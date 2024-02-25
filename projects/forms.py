




from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Student
from .models import Event

class EventForm(forms.ModelForm):
    def clean_faculty(self):
        faculty = self.cleaned_data['faculty']
        try:
            Faculty.objects.get(name=faculty)
        except Faculty.DoesNotExist:
            raise forms.ValidationError("Invalid faculty member.")
        return faculty
    class Meta:
        model = Event
        fields = ['name','date','club','days','location','faculty','description','intake','highlight_event' ]
class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username','email','password1','password2']
    


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'