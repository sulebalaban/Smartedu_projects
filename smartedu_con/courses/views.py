from django.shortcuts import render
from. models import Course


def course_list(request):
    courses=Course.object.all()
    
    context={
        'courses':courses
    }
    
    
    
    return render(request,'courses.html',context)