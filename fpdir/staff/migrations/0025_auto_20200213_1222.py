# Generated by Django 3.0.2 on 2020-02-13 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0024_division_office'),
    ]

    operations = [
        migrations.AlterField(
            model_name='division',
            name='office',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='divisions', to='staff.Office'),
        ),
    ]
