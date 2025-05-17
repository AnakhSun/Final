from rest_framework import serializers
from .models import User, Fragment, Result


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class FragmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fragment
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
