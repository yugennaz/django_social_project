from rest_framework.viewsets import ModelViewSet
from rest_framework import routers

from .models import Image, User

from .serializers import ImageSerializer, UserSerializer


class ImageViewSet(ModelViewSet):
    serializer_class = ImageSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            following = [
                follower.following for follower in
                self.request.user.following.all()
            ]
            following.append(self.request.user)

            return Image.objects.filter(user__in=following)
        return Image.objects.all()


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


router = routers.SimpleRouter()
router.register(r'images', ImageViewSet, basename='Image')
router.register(r'users', UserViewSet)
api_urls = router.urls
