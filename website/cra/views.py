import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('/home/nauen/env/website/tensorflowWechat')
import weibo
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
# 	return HttpResponse('Hello, Intelligent')


def index(request):
	context = {}
	context['hello'] = 'Hello Word!'
	return render(request, 'cra/index.html', context)

def ML(request):
	return render(request, 'cra/ML.html')
