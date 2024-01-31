from django.views import generic

from . import models


class HomeView(generic.DetailView):
    model = models.Category
    template_name = 'home.html'