from django.contrib import admin
from .models import profile, discussion_room, conversation
# Register your models here.

admin.site.register(profile)
admin.site.register(discussion_room)
admin.site.register(conversation)

