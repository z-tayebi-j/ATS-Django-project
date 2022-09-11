from django.urls import path
from rest_framework.authtoken import views

from .views import CreateInterviewerAPIView

urlpatterns = [
    path('interviewer_signup/', CreateInterviewerAPIView.as_view()),
    # path('edit_applicant/<int:pk>/', UpdateApplicantView.as_view())
]
