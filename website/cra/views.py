import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('/home/nauen/env/website/tensorflowWechat')
#import weibo
import markdown
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.

# def index(request):
# 	return HttpResponse('Hello, Intelligent')

def AppleHome(request):
	return render(request, 'cra/applehome.html')
	
def index(request):
	context = {}
	context['hello'] = 'Hello Word!'
	return render(request, 'cra/index.html', context)

def ML(request):
	return render(request, 'cra/ML.html')

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
