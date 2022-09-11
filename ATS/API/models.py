from django.db import models
from django.contrib.auth import get_user_model


class Applicant(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    age = models.CharField(max_length=10)
    gender = models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=100)
    linkedin_address = models.URLField(default='')
    resume = models.FileField(default='')
    status = models.CharField(choices=[('phone', 'phone'),
                                       ('code', 'code'),
                                       ('technical', 'technical'),
                                       ('final', 'final')
                                       ], max_length=100)


class Interviewer(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    telegram_id = models.CharField(max_length=30)


class Interview(models.Model):
    applicant = models.OneToOneField(Applicant, on_delete=models.CASCADE)
    interviewer = models.ForeignKey(Interviewer, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    type = models.CharField(choices=[('pending', 'pending'),
                                     ('Approved to Interview', 'Approved to Interview'),
                                     ('being interviewed', 'being interviewed'),
                                     ('Approved for Hire', 'Approved for Hire'),
                                     ('rejected', 'rejected')
                                     ], max_length=100)


class Feedback(models.Model):
    interview = models.OneToOneField(Interview, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
