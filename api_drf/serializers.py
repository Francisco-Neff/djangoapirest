from rest_framework import serializers
from .models import User_DRF

class UserDRFSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_DRF
        fields = ['id','email_drf','name_drf']