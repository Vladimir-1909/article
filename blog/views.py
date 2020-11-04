from django.shortcuts import render
from .models import News


def home(request):
    data = {
        'title': 'Главная страница',
        'news': News.objects.order_by('-id')
    }
    return render(request, 'blog/home.html', data)


def contact(request):
    data = {
        'title': 'Страница контакты',
        'contact': 'Контакты'
    }
    return render(request, 'blog/contacti.html', context=data)

