# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from models import sign_up
from forms import signup_form
from django.contrib.auth.hashers import make_password


# Create your views here.
def sign_up_view(request):
    if request.method == "POST":
        form = signup_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            name = form.cleaned_data["name"]
            password = form.cleaned_data["password"]
            user_data = signup_form(username=username, name=name,email=email, password=make_password(password))
            user_data.save()
            return render(request, 'user_created.html')
    else:
        form = signup_form()
    return render(request, 'login/index.html', {'form':form})