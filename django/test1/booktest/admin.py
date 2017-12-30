# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import *

class HeroInfoInline(admin.TabularInline): #TabularInline StackedInline
	model = HeroInfo
	extra =3

class BookInfoAdmin(admin.ModelAdmin):
	list_display = ['pk','btitle','bpub_date']
	list_filter = ['btitle']
	search_fields = ['pk','btitle']
	inlines=[HeroInfoInline]


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)