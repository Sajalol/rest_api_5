# Generated by Django 4.1.5 on 2023-01-08 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_task_due_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='due_date_time',
        ),
    ]
