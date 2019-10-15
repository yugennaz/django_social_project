from django.views.generic import ListView
from . models import Image


class HomeView(ListView):
    model = Image
    context_object_name = 'images'
    template_name = 'home.html'

    # def get_queryset(self):
    #     if self.request.user.is_authenticated:
    #         return Image.objects.filter(user__in=self.request.user.following)
    #     return Image.objects.all
