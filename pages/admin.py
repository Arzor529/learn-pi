from django.contrib import admin
from .models import Lesson, LessonComplete, Award, AwardUnlocked, Quiz, QuizQuestion, QuizAnswer, ProfilePicture, ProfilePictureChosen, Friend, ProfileScratchProject

# Register your models here.
admin.site.register(Lesson)
admin.site.register(LessonComplete)
admin.site.register(Award)
admin.site.register(AwardUnlocked)
admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(QuizAnswer)
admin.site.register(ProfilePicture)
admin.site.register(ProfilePictureChosen)
admin.site.register(Friend)
admin.site.register(ProfileScratchProject)