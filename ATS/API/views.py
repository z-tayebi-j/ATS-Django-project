from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Applicant, Interview, Interviewer, Feedback
from .serializers import ApplicantSerializer, InterviewSerializer, InterviewerSerializer, FeedbackSerializer

# Create your views here.
