# Generated by Django 2.0 on 2018-12-05 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20181205_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='serve_time',
        ),
    ]
