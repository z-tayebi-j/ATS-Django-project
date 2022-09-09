from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from API.models import Interviewer, Feedback, Interview, Applicant


class ApplicantSerializer(ModelSerializer):
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
        Applicant = super().save()
        return Applicant

    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Applicant
        fields = (
            'username', 'password', 'first_name', 'last_name', 'age', 'gender', 'linkedin_address', 'resume', 'status')


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
        Interviewer = super().save()
        return Interviewer

    class Meta:
        model = Interviewer
        fields = ('username', 'password', 'first_name', 'last_name', 'telegram_id')


class InterviewSerializer(ModelSerializer):
    type = serializers.CharField(source='get_type_display')

    class Meta:
        model = Interview
        fields = ('applicant', 'interview', 'date', 'type')


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('interview', 'text')
