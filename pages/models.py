from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Lesson Table - Contains a lesson ID and Title
class Lesson(models.Model):
    lesson = models.CharField(max_length=255)

#Lesson Complete Table - Contains a lesson Complete ID, is associated to a Lesson ID via Foreign Key
#Is associated to a user via Foreign Key and boolean to determine whether it is complete or not
class LessonComplete(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson_complete = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Lessons Complete"

#Award Table -  Contains all of the information to create an award object and is associated to a
#specifc lesson via ForeignKey
class Award(models.Model):
    award = models.CharField(max_length=255)
    award_desc = models.CharField(max_length=255)
    award_desc_locked = models.CharField(max_length=255)
    award_score = models.IntegerField()
    award_url = models.CharField(max_length=255)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Awards"

#Award Unlocked Table - Associated to a specific award and user via Foreign Key
#and contains a boolean to determine whether it is unlocked for that user or not
class AwardUnlocked(models.Model):
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    award_unlocked = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Awards Unlocked"

#Quiz Table - Contains a Lesson ID, Quiz Title and is assoicated to a specific
#Lesson via a ForeignKey
class Quiz(models.Model):
    quiz = models.CharField(max_length=255)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Quizzes"

#Quiz Question Table - Contains all of the questions for specific quizzes associated via ForeignKey
class QuizQuestion(models.Model):
    question = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Quiz Questions"

#Quiz Answer Table - Contains all the answers to specific questions associated via Foreign Key
#and whether each answer is incorrect or correct via a boolean
class QuizAnswer(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name="questions")
    answer = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Quiz Answers"

#Profile Picture Table - Stores images for all profile pictures available to select
class ProfilePicture(models.Model):
    profile_picture_path = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "Profile Pictures"

#Function to select the first profile picture as the default for new users
def getDefaultProfilePic():
    return ProfilePicture.objects.get(id = 1)

#Profile Pictrue Chosen Table - Links to a specific profile picture and user via ForeignKey
class ProfilePictureChosen(models.Model):
    profile_picture = models.ForeignKey(ProfilePicture, on_delete=models.CASCADE, default=getDefaultProfilePic)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Profile Pictures Chosen"

#Friend Table - Contains a specific user and another specific user associated via ForeignKey to create friendship
class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "Friend" )
    class Meta:
        verbose_name_plural = "Friends"

#Profile Scratch Project Table - Contains an iframe path and specific user associated via ForeignKey to allow users to place
#Scratch Projects on their profile
class ProfileScratchProject(models.Model):
    scratch_project_link = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
          verbose_name_plural = "Profile Scratch Projects"