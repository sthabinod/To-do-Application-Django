from django.shortcuts import render
from django.http import HttpResponse
from .models import List
# Create your views here.

def index(request):
  
    
    return render(request,'index.html')
def list_added(request):

    title=request.POST.get('title')
    paragraph=request.POST.get('paragraph')
    title =List(title=title,paragraph=paragraph)
    title.save()
    
    list_show= List.objects.all()
   
    context={
        'list_show':list_show
    }
    # list_routine = AddList.objects.order_by('title')[:100]

    # list_dict={
    #     list_routine:'list_routine'
    # }
    
    return render(request,'main/list_show.html',context)



def list_delete(request):
    list_delete = List.objects.all()
    list_delete.delete()

    list_show= List.objects.all()
   
    context={
        'list_show':list_show
    }
    return render(request,'main/list_show.html',context)
    