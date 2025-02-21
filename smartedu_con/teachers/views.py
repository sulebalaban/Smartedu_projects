from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from teachers.models import Teacher 

class  TeacherListView(ListView): 
   model=Teacher
   template_name='teachers.html'
   context_object_name='teachers'
   
class TeacherDetailView(DetailView):
    model=Teacher 
    template_name='teacher.html'
    context_object_name='teacher'