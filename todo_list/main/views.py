from django.shortcuts import render, redirect, reverse, get_object_or_404
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


def update_item(request, page_pk, item_pk):
    
    item = get_object_or_404(Item, pk=item_pk)
    item.complete = not item.complete  # Toggle the boolean field
    item.save()

    url = reverse('index', args=[page_pk])
    return redirect(url)


def delete_item(request, page_pk, item_pk):
    
    item = get_object_or_404(Item, pk=item_pk)
    item.delete()
    
    url = reverse('index', args=[page_pk])
    return redirect(url)



def new_item(request, list_pk):

    if request.method == 'POST':
        text_body = request.POST.get("text")
        if text_body:
            ls = ToDoList.objects.get(id = list_pk)
            new_item = Item(text=text_body, todo_list=ls)
            new_item.save()
        else:
            return HttpResponse("Name field cannot be empty", status=400)

    url = reverse('index', args=[list_pk])
    return redirect(url)


def delete_list(request, list_pk):

    ls = get_object_or_404(ToDoList, pk=list_pk)
    ls.delete()

    return redirect('home')


#def hello(request):
#    return HttpResponse("hello the app is working correctly!")
