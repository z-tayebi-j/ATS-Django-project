from django.urls import path
from rest_framework.authtoken import views

from .views import CreateInterviewerAPIView, ApplicantViewSet, InterviewViewSet, FeedbackViewSet

urlpatterns = [
    path('interviewer_signup/', CreateInterviewerAPIView.as_view()),
    path('applicant/', ApplicantViewSet.as_view({'get': 'list'})),
    path('applicant/<int:pk>/', ApplicantViewSet.as_view({'get': 'retrieve'})),
    path('interview/', InterviewViewSet.as_view({'get': 'list'})),
    path('interview/<int:pk>/', InterviewViewSet.as_view({'get': 'retrieve'})),
    path('feedback/', FeedbackViewSet.as_view({'get': 'list',
                                               'post': 'create'})),
    path('feedback/<int:pk>/', FeedbackViewSet.as_view({'get': 'retrieve'})),
    # path('edit_applicant/<int:pk>/', UpdateApplicantView.as_view())
]
