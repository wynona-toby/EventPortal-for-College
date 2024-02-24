from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Student
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'location','faculty','club']
class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username','email','password1','password2']
    


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'