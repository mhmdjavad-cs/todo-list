from django.db import models
from django.contrib.auth.models import User


class ToDoList(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None) 
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name='list')
    text = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text






