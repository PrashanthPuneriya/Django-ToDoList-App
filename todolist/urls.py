from django.urls import path, include
from .views import (
    todos_list,
    todos_retrieve,
    todos_create,
    todos_update,
    todos_delete,
    todos_search,
)

app_name = 'todolist'

urlpatterns = [
    path('', todos_list, name='index'),
    path('create/', todos_create, name='todosCreate'),
    path('search/', todos_search, name='todosSearch'),
    path('<int:pid>/', todos_retrieve, name='todosGet'),
    path('<int:pid>/update/', todos_update, name='todosUpdate'),
    path('<int:pid>/delete/', todos_delete, name='todosDelete'),
]
