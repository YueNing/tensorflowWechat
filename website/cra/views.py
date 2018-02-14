import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('/home/nauen/tensorflowWechat')
import weibo
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
# 	return HttpResponse('Hello, Intelligent')


def index(request):
	context = {}
	context['hello'] = 'Hello Word!'
	return render(request, 'admin/index.html', context)

def ML(request):
	return render(request, 'cra/ML.html')

def Gallery(request):
	return render(request, 'cra/gallery.html')