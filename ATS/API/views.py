from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, authentication
from rest_framework.response import Response

from .models import Applicant, Interview, Interviewer, Feedback
from .serializers import ApplicantSerializer, InterviewSerializer, InterviewerSerializer, FeedbackSerializer


class CreateInterviewerAPIView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Interviewer
    serializer_class = InterviewerSerializer


class ApplicantViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicantSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.interviewer
        return Interview.objects.filter(interviewer=user).values('applicant')

    def perform_create(self, serializer):
        user = self.request.user
        interviewer = user.interviewer
        serializer.save(interviewer=interviewer)


class InterviewViewSet(viewsets.ModelViewSet):
    serializer_class = InterviewSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.interviewer
        return Interview.objects.filter(interviewer=user)

    def perform_create(self, serializer):
        user = self.request.user
        interviewer = user.interviewer
        serializer.save(interviewer=interviewer)


class FeedbackViewSet(viewsets.ModelViewSet):
    serializer_class = FeedbackSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Feedback.objects.filter(interview=user.id)

    def perform_create(self, serializer):
        serializer.save()
