from rest_framework import serializers
from .models import Remind

class RemindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remind
        fields = ('date', 'time', 'message')