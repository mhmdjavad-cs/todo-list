from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import ToDoList, Item

# Create your views here.

def index_view(request, pk):
    ls = ToDoList.objects.get(id = pk)
    items = Item.objects.filter(todo_list=ls)
    return render(request, 'index.html', {'ls': ls, 'items': items})



def home(request):
    ls = ToDoList.objects.all()
    return render(request, 'home.html', {'ls': ls})

def new_todo_list(request):
    
    if request.method == 'POST':
        #print(request.POST.get('name'))
        name = request.POST.get("name")
        if name:
            new_todo_list = ToDoList(name=name)
            new_todo_list.save()
        else:
            return HttpResponse("Name field cannot be empty", status=400)

    
    return redirect('home')




#def hello(request):
#    return HttpResponse("hello the app is working correctly!")
