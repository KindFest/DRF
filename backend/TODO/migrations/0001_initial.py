# Generated by Django 3.2.15 on 2022-08-17 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authapp', '0002_auto_20220817_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('repo_link', models.URLField(max_length=126, null=True)),
                ('users', models.ManyToManyField(to='authapp.Users')),
            ],
        ),
        migrations.CreateModel(
            name='TODO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=2048)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('create_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authapp.users')),
                ('project_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='TODO.projects')),
            ],
        ),
    ]