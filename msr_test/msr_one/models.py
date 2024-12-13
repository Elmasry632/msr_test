from django.db import models
from django.contrib.auth.models import User

class project_model(models.Model):
    project_name = models.CharField(max_length=20)
    project_description = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.project_name
