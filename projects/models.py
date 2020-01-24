from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import date


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextUploadingField(blank=True, default='')
    summary = models.TextField(max_length=120, blank=True, default='')
    date = models.DateField(blank=True, default=date(1111, 11, 11))
    technology = models.CharField(max_length=120)
    image = models.FileField(upload_to='images/')
    github = models.CharField(max_length=100, blank=True, default='')
    link = models.CharField(max_length=100, blank=True, default='')
    priority = models.IntegerField(blank=True, default=1000)
    published = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.title

    def preview(self):
        return self.description[:50]