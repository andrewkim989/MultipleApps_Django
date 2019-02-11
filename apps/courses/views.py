from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import *

def courses(request):
    all_courses = {
        "courses": Course.objects.all()
    }
    return render(request, "course.html", all_courses)

def add_process(request):
    errors = Course.objects.add_validate(request.POST)
    if request.method == 'POST':
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/courses')
        else:
            Course.objects.create(name = request.POST['name'], desc = request.POST['desc'])
            return redirect("/courses")

def delete(request, num):
    courseinfo = {
        "course": Course.objects.get(id = num)
    }
    return render(request, "delete.html", courseinfo)

def delete_process(request, num):
    Course.objects.get(id = num).delete()
    return redirect("/courses")

def course(request, num):
    course = Course.objects.get(id = num)
    users = User.objects.all()
    otherusers = course.users.all()
    filtered = list(set(users) - set(otherusers))

    context = {
        "course": course,
        "users": filtered,
        "otherusers": otherusers
    }
    return render(request, "add.html", context)

def adduser(request, num):
    if request.method == 'POST':
        course = Course.objects.get(id = num)
        print(request.POST["student"])
        print(course.users)
        course.users.add(request.POST["student"])
    return redirect("/courses/" + num)