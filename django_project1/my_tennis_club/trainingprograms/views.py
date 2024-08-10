from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def trainingprograms(request):
    template = loader.get_template('trainingprograms.html')
    return HttpResponse(template.render())