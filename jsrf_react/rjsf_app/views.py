from django.shortcuts import render
from django.http import HttpResponse
from .models import Person



# Create your views here.


def index(request):
    return render(request, 'newProject/home.html', context={'persons': Person.objects.all()})
    # return HttpResponse("<h1>Test Text from rjsf_app/views.py<h1>")

