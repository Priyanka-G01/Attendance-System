from django.shortcuts import render,redirect
from .forms import EmployeeForm, AttendanceForm,CreateUserForm
from .models import Employee, Attendance
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.

def welcome(request):
    return render(request, "welcome.html")

@login_required(login_url='employee/login')
def showdata(request):
    return render(request, "show_data.html")

@login_required(login_url='employee/login')
def Adddata(request):
    return render(request, "add_det.html")

@login_required(login_url='employee/login')
def load_form(request):
    form = EmployeeForm
    return render(request, "index.html", {'form': form})

@login_required(login_url='employee/login')
def add(request):
    form = EmployeeForm(request.POST)
    form.save()
    return redirect('/welcome')

@login_required(login_url='employee/login')
def show(request):
    employee = Employee.objects.all
    return render(request, 'show.html', {'employee': employee})

@login_required(login_url='employee/login')
def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})

@login_required(login_url='employee/login')
def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    form.save()
    return redirect('/show')

@login_required(login_url='employee/login')
def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')

@login_required(login_url='employee/login')
def search(request):
    given_name = request.POST['name']
    employee = Employee.objects.filter(ename__icontains=given_name)
    return render(request, 'show.html', {'employee': employee})

@login_required(login_url='employee/login')
def load_attendance(request):
    form = AttendanceForm
    return render(request,"detail.html",{'form':form})
@login_required(login_url='employee/login')
def add_att(request):
    form = AttendanceForm(request.POST)
    form.save()
    return redirect('/welcome')
@login_required(login_url='employee/login')
def show_att(request):
    employee = Attendance.objects.all
    return render(request,'show_att.html',{'employee':employee})
@login_required(login_url='employee/login')
def edit_att(request,id):
    employee = Attendance.objects.get(id=id)
    return render(request,'edit_att.html',{'employee':employee})
@login_required(login_url='employee/login')
def delete_att(request,id):
    employee = Attendance.objects.get(id=id)
    employee.delete()
    return redirect('/show_att')
@login_required(login_url='employee/login')
def change(request, id):
    employee = Attendance.objects.get(id=id)
    OT = employee.OT + float(request.POST['ot1'])
    employee.OT = OT
    hrs = employee.hours + float(request.POST['hours'])
    employee.hours = hrs
    employee.save()
    return redirect('/show_att')

def register(request):
    form = CreateUserForm
    if request.method == 'POST':
        Form = CreateUserForm(request.POST)
        if Form.is_valid():
            Form.save()
            messages.success(request,'User has been registered')
    return render(request,'registration/register.html',{'form':form})

def today(request):
    """Shows todays current time and date."""
    myDate = datetime.datetime.now.strftime("%I:%M%p on %B %d, %Y")
    return render(request, 'show_att.html', { 'date': myDate})