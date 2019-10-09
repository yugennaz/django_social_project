from django.views.generic import ListView
from . models import Image


class HomeView(ListView):
    model = Image
    context_object_name = 'images'
    template_name = 'home.html'