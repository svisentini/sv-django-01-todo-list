from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

from django.views.generic import ListView, CreateView


# Create your views here.
def home(request):
    # return HttpResponse("<h1>Ola Treinaweb !</h1>")
    return render(request, "todos/home.html")


# >> Função foi substituida pela classe TodoListView 

#def todo_list(request):
#    todos = Todo.objects.all()
#    return render(request, "todos/todo_list.html", {
#        "todos": todos
#    })


class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]