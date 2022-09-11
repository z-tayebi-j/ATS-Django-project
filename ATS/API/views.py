from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Applicant, Interview, Interviewer, Feedback
from .serializers import ApplicantSerializer, InterviewSerializer, InterviewerSerializer, FeedbackSerializer


class CreateInterviewerAPIView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Interviewer
    serializer_class = InterviewerSerializer
