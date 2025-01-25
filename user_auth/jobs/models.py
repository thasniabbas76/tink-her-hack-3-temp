from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Resume(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='resume')
    file = models.FileField(upload_to='resumes/')

class JobApplication(models.Model):
    job_seeker = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='applications')
    employer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='job_postings')
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)