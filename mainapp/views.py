from django.views import generic
from .models import Lesson


class IndexView(generic.ListView):
    """
    Index Page. List of lessons.
    """
    template_name = 'index.html'
    model = Lesson
