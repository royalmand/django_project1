from django.urls import path
from . import views

urlpatterns = [
    path('trainingprograms/', views.trainingprograms, name='trainingprograms'),
]