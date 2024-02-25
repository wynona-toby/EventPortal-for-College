from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators  import login_required
from .forms import UserProfileForm
from .models import *
from .forms import CreateUserForm, EventForm
from .decorators import allowed_users
from django.contrib.auth.decorators import login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})

@allowed_users(allowed_roles=['students'])
def dashboard(request):
  return render(request,'dashboard.html')
def navbar(request):
  return render(request,'navbar.html')
def main(request):
  return render(request,'main.html')
def admin_dash(request):
  return render(request,'admin_dash.html')
def approve(request):
  return render(request,'approve.html')
def show_events(request):
  events = Event.objects.all()
  # return render(request, 'show_events.html', {'events': events})
  return render(request, 'show_events.html')
def loginpage(request):
  if request.method =='POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('dashboard')
    else:
      messages.info(request, 'Username or Password Incorrect')
  context={}
  return render(request, 'loginpage.html',context)

def registerpage(request):
  
  form=CreateUserForm()
  if request.method =='POST':
    form=CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      user=form.cleaned_data.get('username')
      messages.success(request, 'Registered Succesfully!')
      return redirect('login')
  context ={'form':form}
  return render(request, 'register.html', context)

def logoutpage(request):
  logout(request)
  return redirect('login')

def approved_events(request):
    # approved_events = Event.objects.filter(approved=True)
    # return render(request, 'approved_events.html', {'approved_events': approved_events})
    return render(request,'approved_events.html')


def student_dash(request):
  return render(request,'student_dash.html')