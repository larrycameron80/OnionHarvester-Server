# Generated by Django 2.0 on 2017-12-12 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dispatcher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='css',
        ),
    ]