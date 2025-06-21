from django import forms
from .models import FA1,FA2,FA3,FA4
from django.contrib.auth.forms import UserCreationForm

class FA1form(forms.ModelForm):
    class Meta:
        model = FA1
        fields = ['slno','name', 'eng', 'kan', 'hin', 'maths', 'sci', 'soc_sci']


class FA2form(forms.ModelForm):
    class Meta:
        model = FA2
        fields = ['eng', 'kan', 'hin', 'maths', 'sci', 'soc_sci']  # exclude slno/name



class FA3form(forms.ModelForm):
    class Meta:
        model = FA3
        fields = ['eng', 'kan', 'hin', 'maths', 'sci', 'soc_sci']
class FA4form(forms.ModelForm):
    class Meta:
        model = FA4 
        fields = [ 'eng', 'kan', 'hin', 'maths', 'sci', 'soc_sci']

# class TeacherRegistrationForm(UserCreationForm):
#     class Meta:
#         model = Teacher
#         fields = ['email', 'password1', 'password2']