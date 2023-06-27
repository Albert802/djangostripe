from django_filters import CharFilter,FilterSet
from .models import Lesson


class LessonFilter(FilterSet):
    class Meta:
        model= Lesson
        fields= '__all__'
        exclude = ['video1','video2','video3','notes','topic','subject','term']

