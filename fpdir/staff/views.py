from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.views.generic.base import View



class StaffView(View):
    def get(self, request):
        offices = Office.objects.all()
        departments = Department.objects.all()
        divisions = Division.objects.all()
        persons = Person.objects.all()

        context = {
            'offices': offices,
            'departments': departments,
            'divisions': divisions,
            'persons': persons,
        }
        return render(request, 'staff/staff.html', context)