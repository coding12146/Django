# accounts / serializers.py
from django.contrib.auth import get_user_model
from rest_framework import serializers
from task.models import Team

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer
    사용자 모델을 위한 Serializer입니다.
    팀(Team) 필드를 SlugRelatedField를 사용하여 팀명(name)으로 표시합니다.
    """
    team = serializers.SlugRelatedField(queryset=Team.objects.all(), slug_field="name")
    class Meta:
        model = User
        fields = ("id", "username", "password", "team")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
