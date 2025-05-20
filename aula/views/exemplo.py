from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from ..models import Person

def person_list(request):
    person = Person.objects.all()
    context = {
        'person': person,
    }
    return render(request, 'exemplo/list.html', context)

class PersonListView(View):
    @staticmethod
    def get(request):
        person = Person.objects.all()
        context={
            'person': person,
        }
        return render(request, 'exemplo/list.html', context)
