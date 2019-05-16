# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def catalog(request):
    pass

def category(request, category):
    id = request.GET.get("page", "1")
    pass

def subcategory(request, category, subcategory):
    id = request.GET.get("page", "1")
    pass