# Generated by Django 3.1 on 2020-08-27 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quesTitle', models.CharField(max_length=255)),
                ('quesDesc', models.TextField()),
                ('sampleInput', models.TextField()),
                ('sampleOutput', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeLang', models.CharField(choices=[('c', 'C'), ('cpp', 'C++'), ('py', 'Python')], max_length=3)),
                ('submission', models.FileField(upload_to='./responses')),
                ('submissionTime', models.DateTimeField(auto_now=True)),
                ('score', models.IntegerField()),
                ('latestSubTime', models.TimeField(default='00:00')),
                ('quesID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.question')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalScore', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(default='example@gmail.com', max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('college', models.CharField(blank=True, max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
