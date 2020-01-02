from django.shortcuts import render
from django.http import HttpResponse

from .models import ToDoList, Item

# Create your views here.

'''
def index(response, name):
    ls = ToDoList().objects.get(name=name)
    items = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br></b1><p>%s</p>" %(ls.name str(item.text)))
'''


def index(response):
    return HttpResponse("<h1>This is the Index Page!</h1>")
