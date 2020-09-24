from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class Gorevli(models.Model):
    employee = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.employee.username

class Task (models.Model):

    title = models.CharField(max_length=80)
    description = RichTextUploadingField()
    label = models.TextField(max_length=80)
    status = models.CharField(max_length=10,blank=True)
    employee = models.TextField(max_length=80)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


