from django.shortcuts import render, redirect
from .models import Team, Student
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    room_list = [
    'C107',
    'C108',
    'C109',
    'C110',
    'C111',
    'C121',
    'C225',
    'C307',
    'C308',
    'C309',
    'C321B1',
    'C321B2',
    'C325',
    'C406',
    'C407',
    'C410',
    'C411',
    'C421A',
    'C422',
    'C423',
    'C425',
    'C525',
    'C625',
    'GroundFloorLab',
    'FirstFloorLab',
    'SecondFloorLab',
    'ThirdFloorLab',
    'FourthFloorLab',
    'SixthFloorLab'
    ]
    context = {'room_list': room_list}
    return render(request, 'pages/index.html', context)

def room_view(request, room_no):
    if not request.user.is_authenticated:
        return redirect('login')
    teams = Team.objects.filter(room_no=room_no)
    context = {'teams': teams, 'room': room_no}
    return render(request, 'pages/room-info.html', context)

def attendance1(request, room_no, year):
    if not request.user.is_authenticated:
        return redirect('login')
    teams = Team.objects.filter(room_no=room_no)
    students = Student.objects.filter(team__in=teams, year=year).order_by('team')
    context = {'students': students, 'no': 1}
    if request.method == 'POST':
        absentees = request.POST.getlist('absentees')
        for ab in absentees:
            student = Student.objects.get(reg_no=ab)
            student.attendance_1 = True
            student.save()
        return redirect('home')
    return render(request, 'pages/attendance.html', context)

def attendance2(request, room_no, year):
    if not request.user.is_authenticated:
        return redirect('login')
    teams = Team.objects.filter(room_no=room_no)
    students = Student.objects.filter(team__in=teams, year=year).order_by('team')
    context = {'students': students, 'no': 2}
    if request.method == 'POST':
        absentees = request.POST.getlist('absentees')
        for ab in absentees:
            student = Student.objects.get(reg_no=ab)
            student.attendance_2 = True
            student.save()
        return redirect('home')
    return render(request, 'pages/attendance.html', context)

def attendance3(request, room_no, year):
    if not request.user.is_authenticated:
        return redirect('login')
    teams = Team.objects.filter(room_no=room_no)
    students = Student.objects.filter(team__in=teams, year=year).order_by('team')
    context = {'students': students, 'no': 3}
    if request.method == 'POST':
        absentees = request.POST.getlist('absentees')
        for ab in absentees:
            student = Student.objects.get(reg_no=ab)
            student.attendance_3 = True
            student.save()
        return redirect('home')
    return render(request, 'pages/attendance.html', context)

def attendance4(request, room_no, year):
    if not request.user.is_authenticated:
        return redirect('login')
    teams = Team.objects.filter(room_no=room_no)
    students = Student.objects.filter(team__in=teams, year=year).order_by('team')
    context = {'students': students, 'no': 4}
    if request.method == 'POST':
        absentees = request.POST.getlist('absentees')
        for ab in absentees:
            student = Student.objects.get(reg_no=ab)
            student.attendance_4 = True
            student.save()
        return redirect('home')
    return render(request, 'pages/attendance.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username (or) Password is incorrect')

    context = {}
    return render(request, 'pages/login.html', context)

def logoutUser(request):
    if not request.user.is_authenticated:
        return redirect('home')
    messages.success(request, f'{request.user} has been succesfully logged out.')
    logout(request)
    return redirect('login')
