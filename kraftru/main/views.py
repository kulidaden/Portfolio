from django.shortcuts import render, redirect
from .models import Task
from .forms import *
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    """
    Підвантажує головний html шаблон для цієї функції для urlpatterns, що в urls.py
    """
    # tasks=Task.objects.order_by('-id')
    return render(request,'menv/index.html',{'title':'Головна сторінка сайту'})

def about(request: HttpRequest) -> HttpResponse:
    """
    Звичайний шаблон для сторінки, в якій фото
    """
    return render(request,'menv/about.html')

def create(request: HttpRequest) -> HttpResponse:
    """
    Ця функція створена для заповнення анкети, у разі коректного заповнення,
    запит зберігається в базі даних та повертається повідомлення про успішне
    виконання. Якщо форма була не коректною, то певетається помилка.
    """
    error=''
    thx=''
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            thx='Дякую за ваш запит! \nМи вам зателефонуємо😁'
        else:
            error = 'Форма була не коректною!'
    else:
        form  = TaskForm()


    context={
        'form': form,
        'error': error,
        'thx':thx
    }
    return render(request,'menv/create.html',context)

