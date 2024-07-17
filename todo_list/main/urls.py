from django.urls import path
from .views import home, index_view, new_todo_list

urlpatterns = [ 
    path('<int:pk>', index_view ,name='index'),
    path('', home, name='home'),
    path('new_todo_list/', new_todo_list, name='new_todo_list' )
]


