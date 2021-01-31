from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

#URLS for all pages across the site including views to perform update functions to the DB
app_name = "pages"
urlpatterns = [
    path('', views.index_view, name="index"),
    path('home/', views.home_view, name="home"),
    path('lessons/', views.lessons_view, name="lessons"),
    path('lessons/minecraft/', views.lessons_minecraft_view, name="lessons-minecraft"),
    path('lessons/minecraft/<lessonID>', views.lessons_minecraft_lesson_view, name="lessons-minecraft-lesson"),
    path('complete_lesson/<lessonID>',views.complete_lesson, name="complete_lesson"),
    path('awards/', views.awards_view, name="awards"),
    path('pi_setup/', views.pi_setup_view, name="pi_setup"),
    path('profile/', views.profile_view, name='profile'),
    path('edit_profile_picture/<profilePicID>',views.edit_profile_pic, name="profile_pic"),
    path('add_friend/', views.add_friend_view, name="add_friend"),
    path('embed_project/', views.embed_project_view, name="embed_project"),
    path('edit_embed_project/', views.edit_embed_project_view, name="edit_embed_project"),
    path('profile/friend/<friendID>', views.profile_friend_view, name="profile_friend"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),

    
]
