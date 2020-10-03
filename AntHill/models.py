from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from PIL import Image
from embed_video.fields import EmbedVideoField


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='avatars', default='rikka4.jpg', blank=True)

	def __str__(self, *args, **kwargs):
		return self.user.username

	
	def save(self, *args, **kwargs):
		super().save()

		img = Image.open(self.avatar.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.avatar.path)


	def get_absolute_url(self):
		return reverse('post_author', kwargs = {
				'id': self.id
			})


class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name



class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=70)
	content = RichTextUploadingField(blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)
	thumbnail = models.ImageField(blank=True, null=True)
	category = models.ManyToManyField(Category, blank=True)
	

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_single', kwargs = {
				'id': self.id
			})

	def get_comments(self):
		return self.comments.all()


class Video(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=70)
	video = EmbedVideoField()
	date = models.DateTimeField(auto_now_add=True)
	category = models.ManyToManyField(Category, blank=True)
	

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('video_single', kwargs = {
				'id': self.id
			})

	def get_comments(self):
		return self.comments.all()







class CommentModel(models.Model):
	post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField(max_length=400)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.content 



class VideoCommentModel(models.Model):
	post = models.ForeignKey(Video, related_name='comments', on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField(max_length=400)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.content 


















