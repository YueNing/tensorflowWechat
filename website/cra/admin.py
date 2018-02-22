from django.contrib import admin
from cra.models import *
# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
	pass

admin.site.register(Gallery_user)
admin.site.register(Gallery_details)
admin.site.register(Post)
admin.site.register(Categorie)
