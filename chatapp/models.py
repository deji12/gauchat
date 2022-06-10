from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=100, blank=True, null=True)
    dob = models.CharField(max_length=100,blank=True, null=True)
    address = models.CharField(max_length=1000,blank=True, null=True)
    website = models.CharField(max_length=1000, blank=True, null=True)
    facebook = models.CharField(max_length=1000, blank=True, null=True)
    instagram = models.CharField(max_length=1000, blank=True, null=True)
    twitter = models.CharField(max_length=1000, blank=True, null=True)
    linkedin = models.CharField(max_length=1000, blank=True, null=True)
    picture = models.FileField(blank=True, null=True, upload_to='profileimage/')
    last_seen = models.BooleanField(default=False)
    group = models.BooleanField(default=False)
    two_factor = models.BooleanField(default=False)
    view_profile_pic = models.BooleanField(default=False)
    logged_in_device_setting = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

# class Task(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     task_name = models.CharField(max_length=1000, blank=True, null=True)
#     task_detail = models.CharField(max_length=10000, null=True, blank=True)
#     status = models.BooleanField(default=False)
#     date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return str(self.user)

# class Note(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     note_name = models.CharField(max_length=1000, blank=True, null=True)
#     note_detail = models.CharField(max_length=10000, null=True, blank=True)
#     tag = models.CharField(max_length=1000, blank=True, null=True)
#     date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return str(self.user)