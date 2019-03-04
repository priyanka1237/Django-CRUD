import re
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from core1.models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required


@login_required()
def xyz1(request):
    template ='core1/temp1.html'
    ob=Employee.objects.all()
    context={
        "a":ob
    }
    return render(request,template,context)


@login_required()
def emp_detail(request,pk):
    q=Employee.objects.get(id=pk)
    template="core1/emp_detail.html"
    return render(request,template,{"q":q})

@login_required()
def emp_delete(request,pk):
    q=Employee.objects.get(id=pk)
    q.delete()
    return redirect("xyz1")


@login_required()
def emp_form(request):
    form= EmployeeForm(request.POST)
    if form.is_valid():
        abcd=form.save(commit=False)
        abcd.save()
        return redirect("xyz1")
    template="core1/emp_form.html"
    return render(request,template,{'form':form})

    
@login_required()
def emp_update(request,pk):
    q= get_object_or_404(Employee, id=pk)
    if request.method=="POST":

        form= EmployeeForm(request.POST, instance=q)
        if form.is_valid():
            abcd=form.save(commit=False)
            abcd.save()
            return redirect('xyz1')
    else:
        form= EmployeeForm(instance=q)

    return render(request,"core1/emp_form.html",{'form':form})




