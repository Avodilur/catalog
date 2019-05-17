# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .models import Category
from .models import Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response
from django.template import RequestContext


def products():
    list = Product.objects.all()
    paginator = Paginator(list, 12)
    page = request.GET.get('page')
    try:


def catalog(request):
    category = Category.objects.filter(parent=0)


def category(request, category):
    id = request.GET.get("page", "1")
    category = Category.objects.get(name=category).id
    subcategory = Category.objects.filter(parent=category)


def subcategory(request, category, subcategory):
    id = request.GET.get("page", "1")
    pass