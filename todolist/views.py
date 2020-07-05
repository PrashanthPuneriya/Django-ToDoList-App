from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDo
from .forms import ToDoCreateForm, ToDoSearchForm
from django.contrib.auth.decorators import login_required

# CRUD--> Create, Retrieve, Update, Delete

# Create
@login_required
def todos_create(request):
    # to take input from user we need FORMS
    if request.method == 'POST':
        form = ToDoCreateForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            return redirect("todolist:index")
    else:
        form = ToDoCreateForm()
        context = {"form": form}
        return render(request, "todolist/todos_create.html", context)

# ListALL
@login_required
def todos_list(request):
    user = request.user
    # list_of_todos is a QUERYSET
    # list_of_todos = user.todo_set.all()
    qs = ToDo.objects.filter(user=user)
    
    context = {"todos": qs}
    return render(request, "todolist/todos_list.html", context)

# Retrieve
@login_required
def todos_retrieve(request, pid):
    user = request.user
    qs = ToDo.objects.filter(user=user)
    todo_objs = qs.filter(id=pid)
    context = {"todos": todo_objs}
    return render(request, "todolist/todos_retrieve.html", context)

# Update
@login_required
def todos_update(request, pid):
    user = request.user
    qs = ToDo.objects.filter(user=user)
    todo_obj = qs.get(id=pid)
    if request.method == 'POST':
        form = ToDoCreateForm(request.POST, instance=todo_obj)
        if form.is_valid():
            form.save()
            return redirect("todolist:index")
    else:
        form = ToDoCreateForm(instance=todo_obj)
        context = {"form": form}
    return render(request, "todolist/todos_update.html", context)

# Delete
@login_required
def todos_delete(request, pid):
    user = request.user
    qs = ToDo.objects.filter(user=user)
    todo_obj = qs.get(id=pid)
    todo_obj.delete()
    return redirect("todolist:index")

# Search
@login_required
def todos_search(request):
    if request.method == 'POST':
        form = ToDoSearchForm(request.POST)
        if form.is_valid():
            user = request.user
            todo_name = form.cleaned_data.get("name")

            qs = ToDo.objects.filter(user=user)

            todo_objs = qs.filter(name__icontains=todo_name)

            context = {"todos": todo_objs, "searchedItem": todo_name}
            return render(request, "todolist/todos_retrieve.html", context)
    else:
        form = ToDoSearchForm()
        context = {"form": form}
    return render(request, "todolist/todos_search.html", context)
