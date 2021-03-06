from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(CommentModel)
admin.site.register(Video, MyModelAdmin)
admin.site.register(VideoCommentModel)

