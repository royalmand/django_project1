from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def trainingprograms(request):
    template = loader.get_template('trainingprograms.html')
    return HttpResponse(template.render())

def tpnewbiejangantakut(request):
    template = loader.get_template('tpnewbiejangantakut.html')
    return HttpResponse(template.render())

def tpmbamas(request):
    template = loader.get_template('tpmbamas.html')
    return HttpResponse(template.render())



