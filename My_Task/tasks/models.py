from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    due_date = models.DateField()
    category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title
