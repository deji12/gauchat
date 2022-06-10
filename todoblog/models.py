from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class task_date(models.Model):
    date = models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.date

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=1000, blank=True, null=True)
    task_detail = models.CharField(max_length=10000, null=True, blank=True)
    status = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    parent_date = models.ForeignKey(task_date, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.user)
