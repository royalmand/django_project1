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

def tptandingserius(request):
    template = loader.get_template('tptandingserius.html')
    return HttpResponse(template.render())

def trainingschedules(request):
    template = loader.get_template('trainingschedules.html')
    return HttpResponse(template.render())



