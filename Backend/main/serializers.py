from rest_framework import serializers
from .models import *

class UserTechSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserTech
        fields = ['id', 'name']

class DevicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Devices
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = '__all__'

class CommentsGetSerializer(serializers.ModelSerializer):
    userFK = UserTechSerializer(read_only=True)
    deviceFK = DevicesSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = '__all__'

