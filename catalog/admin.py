# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin


from .models import Cpu
from .models import Monitor


admin.site.register(Monitor)
admin.site.register(Cpu)