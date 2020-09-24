from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

# Register your models here.
from .models import Task, Gorevli

class ModelClass:
    description = RichTextUploadingField()

class PostForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

admin.site.register(Task)
admin.site.register(Gorevli)

