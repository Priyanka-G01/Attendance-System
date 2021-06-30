from django import forms
from .models import Employee,Attendance
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = "__all__"

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
