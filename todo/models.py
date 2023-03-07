from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core import validators
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
# Create your models here.

class Task(models.Model):
    CATEGORIES = (
        (0, 'Backend'),
        (1, 'Frontend'),
        (2, 'Database'),
        (3, 'Python'),
        (4, 'Javascript'),
    )

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
    attachments = models.FileField(upload_to='images/', blank=True)
    category = models.IntegerField(choices=CATEGORIES, default=0)
    priority = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=5,)
    completed_percentage = models.IntegerField(default=0)
    completed = models.BooleanField(default=False, blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.title)