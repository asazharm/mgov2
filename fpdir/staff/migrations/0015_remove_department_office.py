# Generated by Django 3.0.2 on 2020-02-13 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0014_auto_20200213_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='office',
        ),
    ]
