from django.db import models

class modeltable(models.Model):
    name=models.CharField(max_length=264)
    email=models.EmailField()
    phone=models.CharField(max_length=264)
    location=models.CharField(max_length=264)
    education=models.CharField(max_length=264)
    internships=models.CharField(max_length=264)
    trainings=models.CharField(max_length=264)
    projects=models.CharField(max_length=264)
    skills=models.CharField(max_length=264)
