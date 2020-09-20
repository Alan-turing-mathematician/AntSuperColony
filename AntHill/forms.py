from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User






class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']



class AuhorUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['avatar']


class CommentForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea(attrs={
		'class': 'form-control',
		'placeholder': 'Type your comment',
		'rows': 4
		}))


	class Meta:
		model = CommentModel
		fields = ('content', )




class CommentVideoForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea(attrs={
		'class': 'form-control',
		'placeholder': 'Type your comment',
		'rows': 4
		}))


	class Meta:
		model = VideoCommentModel
		fields = ('content', )



















