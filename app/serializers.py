from rest_framework import serializers
from .models import *

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model=Form
        fields = ['address', 'email', 'name', 'phone']