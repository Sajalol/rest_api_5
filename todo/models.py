from django.db import models
import datetime
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    images = models.ImageField(upload_to='images/', blank=True)
    due_date_time = models.DateField(default=datetime.date.today)
    completed = models.BooleanField(default=False, blank=True,       null=True)
    objects = models.Manager()
    def __str__(self):
        return self.title