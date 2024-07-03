from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login 
from django.urls import reverse
from .models import User, Menu, Fee
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import RegisterForm

User = get_user_model()

from django.contrib import messages
from django.contrib.auth import authenticate, login

def supervisor_login(request):
    if request.method == "POST":
        email = request.POST.get('supervisor_email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None and user.is_staff is True:
            login(request, user)
            name = user.name
            request.session['name'] = user.name  # Store user's name in session
            return render(request, 'supervisor/index.html')
        else:
            messages.error(request, "Wrong credentials")
            return render(request, "supervisor/login.html", {'error': "Wrong credentials"})

    return render(request, "supervisor/login.html")



def index(request):
    supervisor = request.user  # Access the authenticated supervisor
    return render(request, 'supervisor/index.html', {'supervisor': supervisor})

def register_student(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'supervisor/register.html', {'form': form, 'success':True, 'attempt':True})
        else:
            return render(request, 'supervisor/register.html', {'form': form, 'success':False, 'attempt':True})
    else:
        form = RegisterForm()
    return render(request, 'supervisor/register.html', {'form': form, 'success':False, 'attempt':False})

def all_students(request):
    students = User.objects.all()  # Fetch all Student objects
    context = {
        'students': students
    }
    return render(request, 'supervisor/all_students.html', context)

def weekly_menu(request):
    menus = Menu.objects.all()
    context = {
        'menus': menus,
    }
    return render(request, 'supervisor/edit_menu.html', context)

def fee_students(request):
    students = Fee.objects.all()  # Fetch all Student objects
    context = {
        'students': students
    }
    return render(request, 'supervisor/fee_students.html', context)

# the following views will handle the server requests to view/delete/update students on run time
def view_student(request, id):
    student = User.objects.get(pk = id)
    return HttpResponseRedirect(reverse('all_students'))

from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import User

def edit(request, id):
    student = User.objects.get(pk=id)
    
    if request.method == "POST":
        form = RegisterForm(request.POST, instance=student)
        if form.is_valid():  # Note the parentheses after is_valid
            form.save()
            return render(request, 'supervisor/edit_student.html', {
                'form': form,
                'success': True
            })
    else:
        form = RegisterForm(instance=student)
    
    return render(request, 'supervisor/edit_student.html', {
        'form': form,
    })


def delete(request, id):
    if request.method == "POST":
        student = User.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('all_students'))

        
