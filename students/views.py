from django.shortcuts import render, redirect
from .models import Student
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def home(request):
    students = Student.objects.all()
    return render(request, 'students/home.html', {'students': students})


def add_students(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        course = request.POST['course']

        Student.objects.create(
            name=name,
            age=age,
            email=email,
            course=course
        )

        return redirect('/')

    return render(request, 'students/add.html')
# username=Dharm_123 and password=Dharm@123

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'students/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'students/login.html')


def logout_user(request):
    logout(request)
    return redirect('/login/')
