from django.http import HttpResponse,JsonResponse

from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse 
# Create your views here.
def index(request):

	 return render(request,'index.html')
