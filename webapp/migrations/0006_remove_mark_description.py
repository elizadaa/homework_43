# Generated by Django 2.1.4 on 2018-12-20 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20181220_0853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark',
            name='description',
        ),
    ]
