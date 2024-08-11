from django.urls import path
from . import views

urlpatterns = [
    path('trainingprograms/', views.trainingprograms, name='trainingprograms'),
    path('trainingprograms/newbie-jangan-takut', views.tpnewbiejangantakut, name='tpnewbiejangantakut'),
    path('trainingprograms/mba-mas', views.tpmbamas, name='tpmbamas'),
]