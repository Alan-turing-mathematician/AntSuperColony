
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
import random 
from django.core.paginator import *
from django.db.models import Count, Q




# ГЛАВНАЯ МУРАВЬИНАЯ СТРАНИЦА
def HomePage(request):
	latest_posts_two = Post.objects.order_by('-date')[0:2]
	latest_posts_five = Post.objects.order_by('-date')[2:5]
	latest_posts = Post.objects.order_by('-date')
	paginator = Paginator(latest_posts, 5)

	latest_video_one = Video.objects.order_by('-date')[0:1]
	latest_video_five = Video.objects.order_by('-date')[0:5]

	page = request.GET.get('page')
	latest_posts = paginator.get_page(page)

	context = {
		'video1': latest_video_one,
		'video5': latest_video_five,
		'latest': latest_posts,
		'latest_two': latest_posts_two
	}
	return render(request, 'index.html', context)


# СТРАНИЦА МУРАВЬИНОГО ПОСТА 
def PostSingle(request, id):
	post = get_object_or_404(Post, id=id)
	latest_posts_two = Post.objects.order_by('-date')[0:2]

	

	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			form.instance.author = request.user
			form.instance.post = post
			form.save()


	else:
		form = CommentForm()



	context = {
		'form': form,
		'latest_two': latest_posts_two,
		'post': post
	}
	return render(request, 'single-post.html', context)


# СТРАНИЦА МУРАВЬИНОГО ВИДЕО
def VideoSingle(request, id):
	post = get_object_or_404(Video, id=id)
	latest_posts_two = Post.objects.order_by('-date')[0:2]

	

	if request.method == 'POST':
		form = CommentVideoForm(request.POST)

		if form.is_valid():
			form.instance.author = request.user
			form.instance.post = post
			form.save()


	else:
		form = CommentVideoForm()



	context = {
		'form': form,
		'latest_two': latest_posts_two,
		'post': post

	}
	return render(request, 'single-video.html', context)



# СТРАНИЦА РЕГЕСТРАЦИИ МУРАВЬИНЫХ ПОЛЬЗОВАТЕЛЕЙ
class UserRegisterPage(CreateView):
	model = User
	email = models.EmailField()
	fields = ['username', 'email', 'password']


# СТРАНИЦА СОЗДАНИЯ МУРАВЬИНЫХ ПОСТОВ
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ('title', 'content', 'thumbnail')

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

# СТРАНИЦА СОЗДАНИЯ МУРАВЬИНЫХ ВИДЕО
class VideoCreateView(LoginRequiredMixin, CreateView):
	model = Video
	fields = ('video', 'title')

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	

# СТРАНИЦА ПРОФИЛЯ МУРАВЬИНЫХ ПОЛЬЗОВАТЕЛЕЙ
@login_required
def UserProfilePage(request):
	profile = Profile.objects.filter(user=request.user)
	if request.method == 'POST':

		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = AuhorUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()


	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = AuhorUpdateForm(instance=request.user)
	context = {
		'profile': profile,
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'profile.html', context)




'''class PostDeleteView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ('title', 'content')

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)'''

# СТРАНИЦА ПРОФИЛЯ АВТОРА МУРАВЬИНОГО ПОСТА
def PostAuthorProfileView(request, id):
	profile = get_object_or_404(Profile, id=id)
	context = {
		'profile': profile
	}
	return render(request, 'post-author.html', context)



