from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class profile(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name="profile")
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    register_no = models.CharField(max_length=10, null=True, blank=True)
    profile_pic = models.ImageField( default="../media/users/user_avtar.webp", null=True, blank=True, upload_to='users/')

class discussion_room(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="room_created")
    name = models.CharField(max_length= 100, blank=True, null=True)
    description = RichTextField(null=True, blank=True)
    conversation_no = models.IntegerField(default=0)
    cover_img = models.ImageField( default="../media/discussion_room/download.jpeg", null=True, blank=True, upload_to='discussion_room/') 

    def __str__(self) :
        return self.name

class conversation(models.Model) :
    group = models.ForeignKey(discussion_room, on_delete=models.CASCADE, blank=True, null=True, related_name="conversations")
    post_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_conversation")
    # text = models.TextField(blank=True, null=True)
    text = RichTextField(blank=True, null=True)

    def __str__(self) :
        return self.post_user.username

