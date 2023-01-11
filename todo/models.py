from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    due_date = models.DateField(default=datetime.date.today,)
    created_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name="todo_created_by",
        on_delete=models.CASCADE,
    )
    assigned_to = models.ForeignKey(
        User,
        blank=True,
        null=True,
        related_name="todo_assigned_to",
        on_delete=models.CASCADE,
    )
    attachements = models.FileField(upload_to='images/', blank=True)
    completed = models.BooleanField(default=False, blank=True,       null=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.title)