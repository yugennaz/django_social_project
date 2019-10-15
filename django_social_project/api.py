from rest_framework.viewsets import ModelViewSet
from rest_framework import routers

from .models import Image, User

from .serializers import (
    ImageSerializer, UserSerializer, UserDetailSerializer
)


class MultiSerializerViewSetMixin(object):
    def get_serializer_class(self):
        """
        Look for serializer class in self.serializer_action_classes, which
        should be a dict mapping action name (key) to serializer class (value),
        i.e.:
        class MyViewSet(MultiSerializerViewSetMixin, ViewSet):
            serializer_class = MyDefaultSerializer
            serializer_action_classes = {
               'list': MyListSerializer,
               'my_action': MyActionSerializer,
            }
            @action
            def my_action:
                ...
        If there's no entry for that action then just fallback to the regular
        get_serializer_class lookup: self.serializer_class, DefaultSerializer.
        """
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super(
                MultiSerializerViewSetMixin, self
            ).get_serializer_class()


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


class UserViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    serializer_action_classes = {
        'list': UserSerializer,
        'retrieve': UserDetailSerializer,
    }


router = routers.SimpleRouter()
router.register(r'images', ImageViewSet, basename='Image')
router.register(r'users', UserViewSet)
api_urls = router.urls
