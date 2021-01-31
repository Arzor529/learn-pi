from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum

#DB tables to be used by the views 
from .models import Lesson, LessonComplete, Quiz, QuizQuestion, QuizAnswer, Award, AwardUnlocked, ProfilePicture, ProfilePictureChosen, Friend, ProfileScratchProject

# Create your views here.

# Login method context
def login_view(request):
    #Check if the request is POST from the login form
    if request.method == 'POST':
        # Store the two variables username and password
        username = request.POST.get('learnPi-username')
        password = request.POST.get('learnPi-password')
        #create a variable using the Django authenticate method
        user = authenticate(username=username, password=password)
        #If details exist and are correct login and send to the homepage
        if user is not None:
            login(request, user)
            return redirect('/home')
        #Else display error and refresh login page
        else:
            messages.error(request,'Sorry, your Username / Password was incorrect.')
            return redirect('/login')           

    return render(request, 'registration/login.html', {})

#logout method

# @login_required sets a login required status on all of these pages - Only accessible to registered users
# If a user somehow accesses the URL by manually typing it etc they will be redirected to the login page

@login_required(login_url='/login')
#take the currently logged in user and end their session using Django logout method
def logout_view(request): #Request is user ID passed by checking current user
    logout(request)
    return redirect('/login')

# Landing Page View - Accessible to all 
def index_view(request):
    return render(request, 'landing/index.html')

# Registered User Home Page View
@login_required(login_url='/login')
def home_view(request):

    # get all lesson objects
    lesson_id = Lesson.objects.all()
    user_id = request.user.id

    # This try catch loads all of the lesson objects and award objects for the current user so that they 
    # are available to them. If they don't exist it then creates them so the user will always be able to
    # see their lessons, awards and whether they have completed/unlocked them
        
    # loop through all lessons and check if the current user has a lesson complete object created
    # if it does get the object, otherwise create it
    for complete in lesson_id: 
        try:
            complete_status = LessonComplete.objects.get(lesson = complete, user = request.user)

        except LessonComplete.DoesNotExist:

            # if the lesson complete object does not exist create it then check if the current user has
            # an award unlocked object created. If it does get it otherwise create it
            complete_status = LessonComplete.objects.create(lesson = complete, user = request.user)
            award_id = Award.objects.filter(lesson = complete)
            for unlocked in award_id:
                try:
                    award_unlocked = AwardUnlocked.objects.get(award = unlocked, user = request.user)

                except AwardUnlocked.DoesNotExist:
                    award_unlocked = AwardUnlocked.objects.create(award = unlocked, user = request.user)
                    award_unlocked.save()
            complete_status.save()

    return render(request, 'home.html')

# Registered User Lessons Home Page View - Overall view of all Lesson topics
@login_required(login_url='/login')
def lessons_view(request):
    return render(request, 'lessons.html')

# Registered User Minecraft Lessons Home Page View - All lessons for Minecraft Lesson topic
@login_required(login_url='/login')
def lessons_minecraft_view(request):
    return render(request, 'lessons-minecraft.html')

#Registered User Minecraft Lesson Page View - Lesson Template for Minecraft Lesson
@login_required(login_url='/login')
def lessons_minecraft_lesson_view(request, lessonID):
    
    #store variables for Quiz based on lesson ID and pass them to lesson page
    quiz = Quiz.objects.get(lesson = lessonID)
    quizQuestion = QuizQuestion.objects.filter(quiz = quiz.id)
    quizAnswer = QuizAnswer.objects.all()

    MC_lesson_context = {
        "quiz" : quiz, "quizQuestion": quizQuestion, "quizAnswer" : quizAnswer}
    return render(request, 'lessons-minecraft-lesson.html', MC_lesson_context)

# View to update the DB with a lesson complete status
@login_required(login_url='/login')
def complete_lesson(request, lessonID):

    #complete lesson function
    #If request is post, pass the lesson ID and filter it to the current user
    if request.method=='POST':
        lesson_id = Lesson.objects.get(id = lessonID)
        user_id = request.user.id
        lesson_complete = Lesson.objects.filter(id = lesson_id.id)
        
        #If a lesson complete status exists for that user return store it in a variable
        for complete in lesson_complete:
            try:
                complete_status = LessonComplete.objects.get(lesson = lesson_id, user = request.user)
            #else create it first, save it and store it
            except LessonComplete.DoesNotExist:
                complete_status = LessonComplete.objects.create(lesson = lesson_id, user = request.user)
                complete_status.save()
        #Set the lesson to complete if not previosuly completed
        if(complete_status.lesson_complete != True):
            complete_status.lesson_complete = True
            complete_status.save()
        #store award variables filtered by lesson ID and user
        award_id = Award.objects.get(lesson = lesson_id)
        award_unlocked = Award.objects.filter(id = award_id.id)
        #If award unlocked status exists get it and store it in a variable
        for unlocked in award_unlocked:
            try:
                unlocked_status = AwardUnlocked.objects.get(award = award_id, user = request.user)
                #else create it and store it 
            except AwardUnlocked.DoesNotExist:
                unlocked_status = AwardUnlocked.objects.create(award = award_id, user = request.user)
                unlocked_status.save()
        #Set award for that lesson and user to unlocked unless previously unlocked.
        if(unlocked_status.award_unlocked != True):
            unlocked_status.award_unlocked = True
            unlocked_status.save()
        
        return redirect('/lessons/minecraft')

# Awards Page View
@login_required(login_url='/login')
#filter awards to display on awards page by user and pass to context
def awards_view(request):
    user_id = request.user.id
    award = Award.objects.all()
    award_unlocked = AwardUnlocked.objects.filter(user = user_id)
    award_context = {"award" : award, "awardUnlocked": award_unlocked}
    return render(request, 'awards.html', award_context)

# Registered User Profile Page
@login_required(login_url='/login')
def profile_view(request):
    #set current user to personalise content on profile page
    current_user = request.user

    if request.user.is_authenticated:
        user_id = current_user.id
        user_fname = current_user.first_name
        username = current_user.username
    #filter profile picture by user
    profile_picture = ProfilePicture.objects.all()
    profile_picture_chosen = ProfilePictureChosen.objects.filter(user = user_id)

    # Pass award data to profile view for printing badges filtered by user

    award_unlocked = AwardUnlocked.objects.order_by("-id").filter(user = user_id)[:3]

    award_unlocked_count = AwardUnlocked.objects.filter(user = user_id, award_unlocked= True).count()
   
    # get score filtered by user based on unlocked awards and dsiplay numer of points or 0 rather than null
    award_unlocked_true = AwardUnlocked.objects.filter(user = user_id)
    award_unlocked_true_filter = award_unlocked_true.filter(award_unlocked = True)
    award_score = award_unlocked_true_filter.aggregate(score=Sum('award__award_score'))['score'] or 0

    #Display friends list 
    friend = Friend.objects.filter(user = user_id)
    friend_uname_id = Friend.objects.filter(user = user_id)

    #function to filter friends list profile pictures in ordered list based on friend user ID
    test = []
    for f in friend_uname_id:
        x = ProfilePictureChosen.objects.get(user=f.friend)
        test.append({'name': f.friend.username, 'pic': x.profile_picture.profile_picture_path})
    
    #Filter scratch projects by user
    scratch_link = ProfileScratchProject.objects.filter(user = user_id)

    scratch_link_count = ProfileScratchProject.objects.filter(user = user_id).count()

    profile_context = {"user": current_user, "uid" : user_id, "ufname" : user_fname, "uname" : username, 
                       "prfpic": profile_picture, "prfpiccho": profile_picture_chosen, "awardUnlocked": award_unlocked, 
                       "awardUnlockedCount" : award_unlocked_count, "awardScore" : award_score, "friend" : friend, "friendPic" : test,
                        "scratchLink" : scratch_link, "scratchLinkCount" : scratch_link_count}

    return render(request, 'profile.html', profile_context)

# View to update the DB with user's new profile picture to select it and display it
@login_required(login_url='/login')
def edit_profile_pic(request, profilePicID):
    #if request is post get selected profile pic and current user
    if request.method=='POST':
        profile_pic_id = ProfilePicture.objects.get(id = profilePicID)
        user_id = request.user.id
        profile_pic_changed = ProfilePicture.objects.filter(id = profile_pic_id.id)
        
        #if profile picture selected status exists get it and store it
        for changed in profile_pic_changed:
            try:
                changed_status = ProfilePictureChosen.objects.get(user = request.user)
            #else create it, save it and store it
            except ProfilePictureChosen.DoesNotExist:
                changed_status = ProfilePictureChosen.objects.create(profile_picture = profile_pic_id, user = request.user)
                changed_status.save()
            #Set profile picture selected to new profile pic passed in POST request
            changed_status.profile_picture = profile_pic_id
            changed_status.save()
        
        #Display success message and redirect to profile
        messages.success(request,'Profile Picture Successfully changed!', extra_tags="profile_pic")
        return redirect('/profile/')

# View to add a friend based on username
@login_required(login_url='/login')
def add_friend_view(request):

    #set current user
    user_id = request.user.id

    #if request is POST get friend username from input box passed in POST request
    if request.method=='POST':
       
        funame = request.POST.get('learnPi-friend-uname')

        #if friend user name for the current user exists, get it and store it
        if User.objects.filter(username = funame).exists():
           friend_uname = User.objects.get(username = funame)
           #If not exists create the friend for the current user, store it and send a success message
           if not Friend.objects.filter(user = request.user, friend = friend_uname).exists():
               
               friend_status = Friend.objects.create(user = request.user, friend = friend_uname)
               friend_status.save()
               messages.success(request,'You have added ' + funame + '!', extra_tags="add_friend")
            #If friendship already exists send message 
           else: 
               messages.success(request,'You are already friends with ' + funame + '!', extra_tags="add_friend")
        #If user doesn't exist error handle
        else:
            messages.error(request,'User does not exist!', extra_tags="add_friend")
    #redirect to friends list
    return redirect('/profile/#badges-friends')

# View to add a scratch project embed link
@login_required(login_url='/login')
def embed_project_view(request):
    #Get current user
    user_id = request.user
    #If request is post, take Iframe from POST request and store it
    if request.method=='POST':
       
        scratch_iframe = request.POST.get('learnPi-scratch-project')

        #If user does not have a SCratch project embedded, create a scratch project DB entry for the current user
        #Pass in the iFrame and save it. Display success message.
        if not ProfileScratchProject.objects.filter(user = user_id).exists():
           print("This object does not exist and will be created")
           user_scratch_iframe = ProfileScratchProject.objects.create(user = user_id, scratch_project_link = scratch_iframe)
           user_scratch_iframe.save()
           messages.success(request,'You have successfully embeded your Scratch Project!', extra_tags="add_project_success")
    #Redirect to user scratch Projects
    return redirect('/profile/#projects')

# View to edit a scratch project embed link
@login_required(login_url='/login')
def edit_embed_project_view(request):
    #Get current user
    user_id = request.user
    #If request is POST take new iFrame and store it
    if request.method=='POST':
       
        scratch_iframe = request.POST.get('learnPi-scratch-project-edit')

        #Check if an iFrame currently exists, if so replace it with new iframe and save, display success message
        if ProfileScratchProject.objects.filter(user = user_id).exists():
            print("Object exists, editing iframe now")

            scratch_project = ProfileScratchProject.objects.get(user = user_id)

            scratch_project.scratch_project_link = scratch_iframe

            scratch_project.save()

            messages.success(request,'You have successfully changed your embedded Scratch Project!', extra_tags="edit_project_success")

            #If doesn't exist, create, pass iframe from POST and save it, display success message
            if not ProfileScratchProject.objects.filter(user = user_id).exists():
               print("This object does not exist and will be created")
               user_scratch_iframe = ProfileScratchProject.objects.create(user = user_id, scratch_project_link = scratch_iframe)
               user_scratch_iframe.save()
               messages.success(request,'You have successfully embedded your Scratch Project!', extra_tags="add_project_success")

    return redirect('/profile/#projects')

# Friend's profile page - Display's friend's personalised content to current user
@login_required(login_url='/login')
#This page is only accessible from the current user's profile so we can pass the current user
#and the ID of the friend from the profile page to display the friend's content here
def profile_friend_view(request, friendID):
    
    #Current user here is equal to the friend you are viewing
    current_user = User.objects.get(username = friendID)
    user_fname = current_user.first_name
    username = current_user.username

    #filter awards unlocked by friend ID for most recent 3 awards
    award_unlocked = AwardUnlocked.objects.order_by("-id").filter(user = current_user)[:3]
    #Count function for displaying either an award or message to say there are no awards unlocked yet
    award_unlocked_count = AwardUnlocked.objects.filter(user = current_user, award_unlocked= True).count()
   
    #get score filtered by user based on unlocked awards and dsiplay numer of points or 0 rather than null
    award_unlocked_true = AwardUnlocked.objects.filter(user = current_user)
    award_unlocked_true_filter = award_unlocked_true.filter(award_unlocked = True)
    award_score = award_unlocked_true_filter.aggregate(score=Sum('award__award_score'))['score'] or 0

    #filter profile picture for display by Friend ID
    profile_picture = ProfilePicture.objects.all()
    profile_picture_chosen = ProfilePictureChosen.objects.filter(user = current_user)
    #Filter username by friend ID
    friend_uname_id = Friend.objects.filter(user = current_user)

    #Display Friend's friend list in order of friend added and display profile pics accordingly
    test = []
    for f in friend_uname_id:
        x = ProfilePictureChosen.objects.get(user=f.friend)
        test.append({'name': f.friend.username, 'pic': x.profile_picture.profile_picture_path})
    
    #filter scratch project by friend ID
    scratch_link = ProfileScratchProject.objects.filter(user = current_user)
    #Count function for displaying message if empty or show scratch project
    scratch_link_count = ProfileScratchProject.objects.filter(user = current_user).count()

    profile_friend_context = {"user": current_user, "ufname" : user_fname, "uname" : username, 
                       "prfpic": profile_picture, "prfpiccho": profile_picture_chosen, "awardUnlocked": award_unlocked, 
                       "awardUnlockedCount" : award_unlocked_count, "awardScore" : award_score, "friendPic" : test,
                       "scratchLink" : scratch_link, "scratchLinkCount" : scratch_link_count}

    return render(request, 'profile-friend.html', profile_friend_context)

# Pi-Setup Page View
@login_required(login_url='/login')
def pi_setup_view(request):
    return render(request, 'pi-setup.html')