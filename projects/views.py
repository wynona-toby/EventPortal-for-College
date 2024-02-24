from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators  import login_required


def dashboard(request):
  return render(request,'dashboard.html')
def navbar(request):
  return render(request,'navbar.html')
def main(request):
  return render(request,'main.html')