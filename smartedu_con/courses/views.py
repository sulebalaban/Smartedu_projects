from django.shortcuts import render,get_object_or_404
from. models import Course,Category,Tag


def course_list(request,category_slug=None,tag_slug=None):
    category_page=None
    tag_page=None
    categories=Category.objects.all()
    tags=Tag.objects.all()
    
    if category_slug != None:
        category_page=get_object_or_404(Category, slug=category_slug)
        courses=Course.objects.filter(available=True, category=category_page)
        
    elif tag_slug != None:
        tag_page=get_object_or_404(Tag, slug=tag_slug)
        courses=Course.objects.filter(available=True, tags=tag_page)
        
    else:
        courses=Course.objects.all().order_by('-date')   
        
             
    context={
        'courses':courses,
        'categories':categories,
        'tags':tags
    }
    
        
    return render(request,'courses.html',context)


def search(request):
    courses=Course.objects.filter(name__contains=request.GET['search'])
    categories=Category.objects.all()
    tags=Tag.objects.all()
    
    context = {
        'courses':courses,
        'categories':categories,
        'tags':tags
    }
         
    return render(request,'courses.html',context)
    
def course_detail(request, category_slug, course_id):
    course = get_object_or_404(Course, id=course_id)
    context = {'course': course}
    return render(request, 'course.html', context)    
    
    
        
