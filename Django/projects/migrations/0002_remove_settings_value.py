# Generated by Django 4.1.3 on 2023-05-30 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='value',
        ),
    ]