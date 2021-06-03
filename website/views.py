from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import TodoItem;

def index(request):
    all_todo_items = TodoItem.objects.all()
    return render(request,'website.html',{'all_items':all_todo_items})

def addTodo(request):
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/website/')

def deleteTodo(request,todo_id):
    deleted_item = TodoItem.objects.get(id=todo_id)
    deleted_item.delete()
    return HttpResponseRedirect('/website/')

from django.shortcuts import render

# Create your views here.
