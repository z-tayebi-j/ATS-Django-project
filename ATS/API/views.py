from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
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
    authentication_classes = []
    permission_classes = []
    queryset = Applicant.objects.all()

    #
    def perform_create(self, serializer):
        user = self.request.user
        interviewer = user.interviewer
        serializer.save(interviewer=interviewer)


class InterviewViewSet(viewsets.ModelViewSet):
    serializer_class = InterviewSerializer
    authentication_classes = []
    permission_classes = []
    queryset = Interview.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        interviewer = user.interviewer
        serializer.save(interviewer=interviewer)
