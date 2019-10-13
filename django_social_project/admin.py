from django.contrib import admin
from .models import Image, User, Follower


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'image']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'first_name', 'last_name'
    ]


@admin.register(Follower)
class FollwerAdmin(admin.ModelAdmin):
    list_display = [
        'follower', 'following'
    ]
