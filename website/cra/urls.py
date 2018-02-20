from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('AppleHome', views.AppleHome, name='AppleHome'),
	path('Vorlesungen/ML', views.ML, name='vorlesung_ML'),
	path('Gallery/Hi', views.Gallery, name='Hi'),
	path('Data/Weibo', views.DataWeibo, name='Data_weibo'),
	path('Data/Gallery', views.DataGallery, name='Data_gallery'),
]
