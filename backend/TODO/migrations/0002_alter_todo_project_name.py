# Generated by Django 3.2.15 on 2022-08-17 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TODO', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TODO.projects'),
        ),
    ]
