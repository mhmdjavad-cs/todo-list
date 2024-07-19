from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http.response import HttpResponse
from .models import ToDoList, Item
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User



@login_required
def index_view(request, pk):
    
    try:
        ls = ToDoList.objects.get(pk = pk)
    except ToDoList.DoesNotExist:
        return redirect('home')

    
    if(request.user == ls.user):

        items = Item.objects.filter(todo_list=ls)
        return render(request, 'index.html', {'ls': ls, 'items': items})

    else:
        return redirect('home')


@login_required
def home(request):
    ls = ToDoList.objects.filter(user = request.user)
    return render(request, 'home.html', {'ls': ls})


@login_required
def new_todo_list(request):
    
    if request.method == 'POST':
        #print(request.POST.get('name'))
        name = request.POST.get("name")
        if name:
            new_todo_list = ToDoList(name=name, user=request.user)
            new_todo_list.save()
        else:
            return HttpResponse("Name field cannot be empty", status=400)

    
    return redirect('home')



@login_required
def update_item(request, page_pk, item_pk):
    
    item = get_object_or_404(Item, pk=item_pk)
    item.complete = not item.complete  # Toggle the boolean field
    item.save()

    url = reverse('index', args=[page_pk])
    return redirect(url)



@login_required
def delete_item(request, page_pk, item_pk):
    
    item = get_object_or_404(Item, pk=item_pk)
    item.delete()
    
    url = reverse('index', args=[page_pk])
    return redirect(url)



@login_required
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


@login_required
def delete_list(request, list_pk):

    ls = get_object_or_404(ToDoList, pk=list_pk)
    ls.delete()

    return redirect('home')


def login_user(request):


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'user does not exist!')
            return render(request, 'login.html', {})        
    

    return render(request, 'login.html', {})





def logout_user(request):
    logout(request)
    messages.success(request, 'successfully logged out!')
    return redirect('login')



def signup_user(request):

    if request.method == 'POST':

        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if password1 == password2:
                
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already taken')
                elif User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already taken')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    login(request, user)
                    return redirect('home')

            else:
                messages.error(request, 'passwords didn\'t match, please try again!')
                return redirect('signup')

        except:
            messages.error(request, 'please fill the required fields!')
            return redirect('signup')


    return render(request, 'signup.html', {})


