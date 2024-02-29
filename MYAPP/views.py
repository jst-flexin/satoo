from django.shortcuts import render
from MYAPP.forms import StudentForm


def home(request):
    stud = StudentForm
    return render(request,'index.html',{'form': stud})
#