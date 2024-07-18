from django.urls import path
from .views import home, index_view, new_todo_list, update_item, delete_item, new_item, delete_list, login_user, logout_user

urlpatterns = [ 
    path('<int:pk>', index_view ,name='index'),
    path('', home, name='home'),
    path('new_todo_list/', new_todo_list, name='new_todo_list' ),
    path('update_item/<int:page_pk>/<int:item_pk>', update_item, name='update_item'),
    path('delete_item/<int:page_pk>/<int:item_pk>', delete_item, name='delete_item'),
    path('new_item/<int:list_pk>', new_item, name='new_item'),
    path('delete_list/<int:list_pk>', delete_list, name='delete_list'),
    path('login/<str:massage>', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

]


