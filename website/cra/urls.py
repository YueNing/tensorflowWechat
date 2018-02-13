from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('Vorlesungen/ML', views.ML, name='vorlesung_ML'),
]