from django.contrib import admin
from . import models
from adminsortable.admin import SortableAdmin
from django.urls import reverse


class OfficeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}

class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}

class DivisionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}

class PersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}


admin.site.register(models.Office, SortableAdmin)
admin.site.register(models.Department, SortableAdmin)
admin.site.register(models.Division, SortableAdmin)
admin.site.register(models.Person, SortableAdmin)