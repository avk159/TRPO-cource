from django import forms
from .models import docprofile, Doctor



class RegisterForm(forms.Form):
    login = forms.CharField(label='Логин', min_length=4, max_length=20)
    name = forms.CharField(label='Имя', min_length=4, max_length=20)
    password = forms.CharField(label='Пароль', min_length=5, max_length=20)
    required_css_class = "field"
    error_css_class = "error"

class LoginForm(forms.Form):
    login = forms.CharField(label='Логин', min_length=4, max_length=20)
    password = forms.CharField(label='Пароль', min_length=4, max_length=20)
    required_css_class = "field"
    error_css_class = "error"

class DateInput(forms.DateInput):
    input_type = 'date'

class AppointForm(forms.Form):
    docprofile = docprofile.objects.all()
    Doctor = Doctor.objects.all()
    times = (('1', '08:00'), ('2', '09:00'), ('3', '10:00'), ('4', '11:00'), ('5', '12:00'), ('6', '13:00'), ('7', '14:00'), ('8', '15:00'), ('9', '16:00'))
    profile = forms.ModelChoiceField(label="Выберите профиль", queryset=docprofile)
    doctor = forms.ModelChoiceField(label="Выберите специалиста" ,queryset=Doctor)
    date = forms.DateField(label ="Выберите дату" , input_formats=['%d/%m/%Y'], widget=DateInput)
    time = forms.ChoiceField(label="Выберите время", choices=times)
    required_css_class = "field"
    error_css_class = "error"