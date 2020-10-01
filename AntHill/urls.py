from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as AuthViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage, name='home'),
    path('login/', AuthViews.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', AuthViews.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', UserRegisterPage.as_view(template_name='register.html'), name='register'),
    path('create/', PostCreateView.as_view(template_name='create_post.html'), name='create_post'),
    path('profile_my/', UserProfilePage, name='profile'),
    path('post/<id>/', PostSingle, name='post_single'),
    path('author/<id>/', PostAuthorProfileView, name='post_author'),
    path('video/<id>/', VideoSingle, name='video_single'),


]
