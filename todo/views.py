from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import TodoItem

def index(request):
    all_items = TodoItem.objects.all()
    context = {
            'all_items':all_items
            }
    return render(request,'todo/todo.html',context)


def addTodo(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        new_item=TodoItem(content = content)
        new_item.save()
    return HttpResponseRedirect('/')


def deleteTodo(request,todo_id):
    delete_Todo = TodoItem.objects.get(id = todo_id)
    delete_Todo.delete()
    return HttpResponseRedirect('/')

def contact(request):
    return render(request,'todo/contact.html')

