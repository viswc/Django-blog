from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from MainApp.models import Blog
from pandas import *
import json
from django.conf import settings

def index(request):
	reqBlog = Blog.objects.all()
	return render(request, "Index.html", {
		"blogs": reqBlog,
	})

def list(request, blog_key):
	reqBlog = Blog.objects.filter(primaryKey = blog_key).first()
	if reqBlog is None:
		return HttpResponseRedirect(reverse("Internship:index"))
	else:
		reqRelated = Blog.objects.exclude(primaryKey = blog_key).all()
		return render(request, "List.html", {
			"mainBlog": reqBlog, "related": reqRelated,
		})

def about(request):
	return render(request, "About.html", {
	})