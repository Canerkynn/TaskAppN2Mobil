# Generated by Django 3.1.1 on 2020-09-24 05:00

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
