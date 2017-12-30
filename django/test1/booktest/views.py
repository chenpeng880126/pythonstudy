# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import *
from django.template import RequestContext, loader
from .models import *

def index(request):

	booklist = BookInfo.objects.all()
	context = {'list':booklist}

	return render(request,"booktest/index.html",context)

def show(request,id):

	book = BookInfo.objects.get(pk=id)
	herolist = book.heroinfo_set.all()
	context = {'list':herolist}
	return render(request,"booktest/show.html",context)