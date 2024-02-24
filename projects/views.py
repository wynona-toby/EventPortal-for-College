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

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})

# @allowed_users(allowed_roles=['students'])
def dashboard(request):
  return render(request,'dashboard.html')
def navbar(request):
  return render(request,'navbar.html')
def main(request):
  return render(request,'main.html')
def show_events(request):
  events = Event.objects.all()
  return render(request, 'show_events.html', {'events': events})
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


# @login_required
# def loginpage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             if user.post == 'student' and 'rollno' in request.POST:
#                 # Authenticate user as a student with rollno
#                 # ...
#                 return redirect('dashboard')
#             elif user.post == 'faculty' and 'id' in request.POST:
#                 # Authenticate user as a faculty with id
#                 # ...
#                 return redirect('dashboard')
#             else:
#                 messages.error(request, "Invalid credentials")
#         else:
#             messages.error(request, "Invalid credentials")
#     else:
#         user = request.user
#     return render(request, 'login.html', {'user': user})

# def loginpage(request):
  # User = get_user_model()
  # if request.method =='POST':
  #   username=request.POST.get('username')
  #   password=request.POST.get('password')
  #   if User.objects.filter(username=username).exists() or User.objects.filter(username=username, is_student=True).exists() or User.objects.filter(username=username, is_faculty=True).exists():
  #     # Authenticate user
  #     user = authenticate(request, username=username, password=password)
  #     # If user is authenticated
  #     if user is not None:
  #       # Log in user
  #       login(request, user)
  #       # Redirect to dashboard
  #       return redirect('dashboard')
  #     else:
  #       # Display error message
  #       messages.error(request, "Username or Password is incorrect")
  #   else:
  #     # Display error message
  #     messages.error(request, "Username does not exist in student or faculty table")
  # # Render login template
  # return redirect('dashboard')