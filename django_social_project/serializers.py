from rest_framework import serializers

from .models import Image, User


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class UserDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    followers = serializers.ReadOnlyField(source='followers.count')
    following = serializers.ReadOnlyField(source='following.count')

    class Meta:
        model = User
        fields = ['username', 'images', 'followers', 'following']
