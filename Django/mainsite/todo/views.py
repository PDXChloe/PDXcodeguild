from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def index(request):

    # print(request.method)
    # print(request.body)
    # print(request.GET)

    # name
    #
    # output = '<html><head></head><body>'
    # output += '<ul>'
    #
    # for i in range(100):
    #     output += '<li>{i}</li>'
    # output += '</body></html>'
    # print(output)
    # return HttpResponse('Hello World')

    # todo_items = TodoItem.objects.all()
    #
    # output = '<html><head></head><body>'
    # output += "<ul>"
    #
    # for todo_item in todo_items:
    #     # print(todo_item.todo_text)
    #     output += f'<li>{todo_item.todo_text}</li>'
    # output += '</ul>'
    # output += '</body></html>'
    # return HttpResponse(output)

    todo_items = TodoItem.objects.all()
    context = {"todo_items": todo_items}

    return render(request, 'todo/index.html', context)


def savetodo(request):
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(todo_text=todo_text)
    todo_item.save() #saving new item into database

    return HttpResponseRedirect(reverse('todo:index'))
