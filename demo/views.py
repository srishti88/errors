# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    text = {'name':'Srishti','age':'23'}
    return render(request,'demo/index.html',context=text)