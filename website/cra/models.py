from django.db import models

# Create your models here.
class Weibo_user(models.Model):
	username = models.CharField(max_length=20)
	user_id = models.UUIDField()
#	weibo_details = models.ForeignKey('Weibo_details', on_delete=models.CASCADE, )

class Weibo_details(models.Model):
	user = models.ForeignKey('Weibo_user', on_delete=models.CASCADE)
	picture_id = models.UUIDField()
	text_url = models.URLField()
	picture_urls = models.URLField()
	picture_details = models.CharField(max_length=300)
	word_cloud_picture = models.URLField()
	word_cloud = models.CharField(max_length=300)

class Gallery_user(models.Model):
	name = models.CharField(max_length=20)
	user_id = models.UUIDField()
#	gallery_details = models.ForeignKey('Gallery_details', on_delete=models.CASCADE, )

class Gallery_details(models.Model):
	user = models.ForeignKey('Gallery_user', on_delete=models.CASCADE)
	picture_id = models.UUIDField()
	picture_urls = models.URLField()
	picture_describes = models.CharField(max_length=300)

class Categorie(models.Model):
	name = models.CharField(max_length=300)
	describe = models.TextField()

class Post(models.Model):
	Categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
	title = models.CharField(max_length=300)
	body = models.TextField()
