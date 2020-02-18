# Generated by Django 3.0.2 on 2020-02-11 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0007_auto_20200211_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.Department'),
        ),
        migrations.AlterField(
            model_name='person',
            name='office',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.Office'),
        ),
    ]
