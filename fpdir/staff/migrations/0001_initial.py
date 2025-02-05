# Generated by Django 3.0.2 on 2020-02-06 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('url', models.SlugField(max_length=120, unique=True)),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('url', models.SlugField(max_length=120, unique=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.Department')),
            ],
            options={
                'verbose_name': 'Division',
                'verbose_name_plural': 'Divisions',
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('url', models.SlugField(max_length=120, unique=True)),
            ],
            options={
                'verbose_name': 'Office',
                'verbose_name_plural': 'Offices',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('surname', models.CharField(max_length=30, verbose_name='Surname')),
                ('birthday', models.DateField(help_text='yyyy-mm-dd', verbose_name='Birthday')),
                ('job_acceptance_date', models.DateField(help_text='yyyy-mm-dd', null=True, verbose_name='Job Acceptance Date')),
                ('image', models.ImageField(upload_to='persons', verbose_name='Image')),
                ('position', models.CharField(max_length=50, verbose_name='Position')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email')),
                ('phone_number', models.PositiveSmallIntegerField(blank=True, null=True, unique=True, verbose_name='Phone')),
                ('url', models.SlugField(max_length=120, unique=True)),
                ('last_update', models.DateField(auto_now=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.Department')),
                ('division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.Division')),
                ('office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.Office')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='office',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.Office'),
        ),
    ]
