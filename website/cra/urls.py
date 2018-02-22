from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('AppleHome', views.AppleHome, name='AppleHome'),
	path('Vorlesungen/ML', views.ML, name='vorlesung_ML'),
	re_path(r'markdown/test/(?P<pk>[\w-]+)$', views.Detail, name='markdown'),
	path('Gallery/Hi', views.Gallery, name='Hi'),
	path('Data/Weibo', views.DataWeibo, name='Data_weibo'),
	path('Data/Gallery', views.DataGallery, name='Data_gallery'),
]
