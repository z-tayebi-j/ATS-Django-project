from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.serializers import ReadOnlyField, ModelSerializer
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework import serializers

from usermanagement.models import Interviewer


class InterviewerSerializer(ModelSerializer):
    username = serializers.CharField(max_length=100, write_only=True)
    password = serializers.CharField(max_length=100, write_only=True)
    first_name = serializers.CharField(max_length=100, write_only=True)
    last_name = serializers.CharField(max_length=100, write_only=True)

    def save(self, **kwargs):
        user_model = get_user_model()
        username = self.validated_data.pop('username')
        password = self.validated_data.pop('password')
        first_name = self.validated_data.pop('first_name')
        last_name = self.validated_data.pop('last_name')

        user = user_model.objects.create_user(username=username, password=password, first_name=first_name,
                                              last_name=last_name)
        Token.objects.create(user=user)
        self.validated_data['user'] = user
        interviewer = super().save()
        return interviewer

    class Meta:
        model = Interviewer
        fields = ('username', 'password', 'first_name', 'last_name', 'telegram_id')


class FeedbackSerializer(ModelSerializer):
    pass


class ApplicantSerializer(ModelSerializer):
    pass


class InterviewSerializer(ModelSerializer):
    pass
