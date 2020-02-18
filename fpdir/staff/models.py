from django.db import models
from datetime import date
from adminsortable.fields import SortableForeignKey
from adminsortable.models import SortableMixin
# from slugify import slugify



class Office(SortableMixin):
    name = models.CharField('Name', max_length=120, db_index=True)
    url = models.SlugField(max_length=120, unique=True, )
    independent = models.BooleanField(default=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Office'
        verbose_name_plural = 'Offices'
        ordering = ['office_order']

    office_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

class Department(SortableMixin):
    name = models.CharField('Name', max_length=120)
    office = SortableForeignKey('Office', on_delete=models.SET_NULL, blank=True, null=True, related_name='departments')
    url = models.SlugField(unique=True, null=True, blank=True)
    independent = models.BooleanField(default=False)

    def __str__(self):
        return self.name



    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        ordering = ['department_order']
    
    department_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)


class Division(SortableMixin):
    name = models.CharField('name', max_length=120, db_index=True)
    office = models.ForeignKey('Office', on_delete=models.SET_NULL, blank=True, null=True, related_name='divisions', db_index=True)
    department = SortableForeignKey('Department', on_delete=models.SET_NULL, blank=True, null=True, related_name='divisions')
    url = models.SlugField(max_length=120, unique=True)
    independent = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Division'
        verbose_name_plural = 'Divisions'
        ordering = ['division_order']

    division_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

class Person(SortableMixin):
    first_name = models.CharField('First Name', max_length=30, db_index=True)
    last_name = models.CharField('Last Name', max_length=30, db_index=True)
    surname = models.CharField('Surname', max_length=30, db_index=True)
    birthday = models.DateField('Birthday', help_text='yyyy-mm-dd', db_index=True)
    job_acceptance_date = models.DateField('Job Acceptance Date', help_text='yyyy-mm-dd', blank=True, null=True)
    image = models.ImageField('Image', upload_to="persons")

    office = models.ForeignKey('Office', on_delete=models.SET_NULL, blank=True, null=True, related_name='persons')
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, blank=True, null=True, related_name='persons')
    division = SortableForeignKey('Division', on_delete=models.SET_NULL, blank=True, null=True, related_name='persons')
    position = models.CharField('Position', max_length=50, db_index=True)

    email = models.EmailField('Email', unique=True, blank=True, null=True, db_index=True)
    phone_number = models.PositiveSmallIntegerField('Phone', unique=True, blank=True, null=True, db_index=True)
    url = models.SlugField(max_length=120, unique=True)
    last_update = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
        ordering = ['person_order']

    person_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

