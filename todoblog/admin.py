from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.Task)
admin.site.register(models.task_date)
