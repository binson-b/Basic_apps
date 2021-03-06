from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignee')
    completed = models.BooleanField('Completed', default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')