# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models


class Monitor(models.Model):
    mon_name = models.TextField()
    mon_diagonal = models.CharField(max_length=5)

    def __str__(self):
        return self.mon_name


class Cpu(models.Model):
    cpu_name = models.CharField(max_length=100)
    cpu_firm = models.CharField(max_length=20)

    def __str__(self):
        return self.cpu_name
