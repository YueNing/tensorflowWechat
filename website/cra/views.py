import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('/home/nauen/env/website/tensorflowWechat')
#import weibo
import markdown
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from .models import Post, Categorie
# Create your views here.

# def index(request):
# 	return HttpResponse('Hello, Intelligent')

def AppleHome(request):
	return render(request, 'cra/applehome.html')
	
def index(request):
	context = {}
	categorie = Categorie.objects.all()
	context['hello'] = 'Hello Word!'
#	import pdb
#	pdb.set_trace()
	return render(request, 'cra/index.html', context={'categorie':categorie})

def ML(request):
	post = Post.objects.get(pk=1)
	categorie = Categorie.objects.all()
	post.body = markdown.markdown(post.body,
					extensions=[
						'markdown.extensions.extra',
						'markdown.extensions.codehilite',
						'markdown.extensions.toc',
						])
	return render(request, 'cra/ML.html',context={'post': post, 'categorie':categorie})

def Gallery(request):
	return render(request, 'cra/gallery.html')

def DataWeibo(request):
	return render(request, 'cra/data_weibo.html')

def DataGallery(request):
	return render(request, 'cra/data_gallery.html')

def Detail(request, pk=1):
	post = get_object_or_404(Post, pk=pk)
	post.body = markdown.markdown(post.body,
					extensions=[
						'markdown.extensions.extra',
						'markdown.extensions.codehilite',
						'markdown.extensions.toc',
						])
	return render(request, 'cra/test.html', context={'post': post})

def page_not_found(request):
    return render_to_response('admin/page_404.html')

def page_error(request):
	return render_to_response('admin/page_500.html')
