from django.db import models

# Create your models here.
class Mylife(models.Model):
    age=models.CharField(max_length=129)
    topic=models.CharField(max_length=129)
    college=models.CharField(max_length=129)
    school=models.CharField(max_length=129)
    rollno=models.CharField(max_length=129)