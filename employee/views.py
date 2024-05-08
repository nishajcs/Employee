from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Employee
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def home(request):
    data = Employee.objects.all()
    return render(request, "employee/list.html", {"employee":data})

@login_required(login_url="login")
def add(request):
    name = request.POST.get("name")
    age = request.POST.get("age")
    job_title = request.POST.get("jobtitle")
    department = request.POST.get("department")
    photo = request.FILES.get("photo")
    if name and age and job_title and department:
        employee = Employee(name=name, age=age, job_title=job_title, department=department, photo=photo)
        employee.save()
        return HttpResponseRedirect("/employee")
    return render(request, "employee/add.html")

@login_required(login_url="login")
def detail(request, id):
    data = Employee.objects.get(pk=id)
    return render(request, "employee/detail.html", {"employee":data})

@login_required(login_url="login")
def delete(request,id):
    data = Employee.objects.get(pk=id)
    data.delete()
    return HttpResponseRedirect("/employee")

@login_required(login_url="login")
def update(request,id):
    data = Employee.objects.get(pk=id) #
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        job_title = request.POST.get("jobtitle")
        department = request.POST.get("department")
        photo = request.FILES.get("photo")
        if name and age and job_title and department:
            data.name = name
            data.age = age
            data.job_title = job_title
            data.department = department
            data.photo = photo
            data.save()
            return HttpResponseRedirect("/employee")
    return render(request, "employee/update.html",{"employee":data})

    