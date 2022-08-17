# Generated by Django 3.2.15 on 2022-08-17 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20220817_1234'),
        ('TODO', '0002_alter_todo_project_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='create_by',
        ),
        migrations.AddField(
            model_name='todo',
            name='create_by',
            field=models.ManyToManyField(to='authapp.Users'),
        ),
    ]
