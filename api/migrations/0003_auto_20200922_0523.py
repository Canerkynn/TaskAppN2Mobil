# Generated by Django 3.1.1 on 2020-09-22 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200922_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.TextField(max_length=80),
        ),
    ]
