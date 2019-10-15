from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Image, User, Follower


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'image']


@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Follower)
class FollwerAdmin(admin.ModelAdmin):
    list_display = [
        'follower', 'following'
    ]
