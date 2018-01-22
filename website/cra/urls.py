from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	# path('cra/', include('cra.urls')),
	# path('admin/', admin.site.urls),
]