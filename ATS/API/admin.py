from django.contrib import admin

from .models import Interviewer, Interview, Applicant, Feedback

admin.site.register(Interview)
admin.site.register(Applicant)
