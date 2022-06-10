from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Note(models.Model):
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    content = models.TextField()
    tag = models.CharField(max_length=100)
    div_name  = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    date_2 = models.DateField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return str(self.author)