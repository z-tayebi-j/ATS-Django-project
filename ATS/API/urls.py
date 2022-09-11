from django.urls import path
from rest_framework.authtoken import views

from .views import CreateInterviewerAPIView, ApplicantViewSet, InterviewViewSet

urlpatterns = [
    path('interviewer_signup/', CreateInterviewerAPIView.as_view()),
    path('applicant/', ApplicantViewSet.as_view({'get': 'list'})),
    path('interview/', InterviewViewSet.as_view({'get': 'list'})),
    # path('edit_applicant/<int:pk>/', UpdateApplicantView.as_view())
]
