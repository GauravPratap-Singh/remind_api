from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RemindSerializer
from .models import Remind

# Create your views here.

class ReminderView(viewsets.ModelViewSet):
    serializer_class = RemindSerializer
    queryset = Remind.objects.all()