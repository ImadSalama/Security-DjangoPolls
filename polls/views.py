from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from polls.models import Question
from polls.serializer import PollsSerializer


# Create your views here.
class PollsViewSet(ModelViewSet):
    serializer_class = PollsSerializer
    queryset = Question.objects.all()
