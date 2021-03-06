# Generated by Django 3.0 on 2020-01-20 21:25

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='')),
                ('summary', models.TextField(blank=True, default='', max_length=120)),
                ('date', models.DateField(blank=True, default=datetime.date(1111, 11, 11))),
                ('technology', models.CharField(max_length=120)),
                ('image', models.FileField(upload_to='images/')),
                ('github', models.CharField(blank=True, default='', max_length=100)),
                ('link', models.CharField(blank=True, default='', max_length=100)),
                ('priority', models.IntegerField(blank=True, default=1000)),
            ],
        ),
    ]
