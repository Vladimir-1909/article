from django.shortcuts import render


def home(request):
    data = {
        'home': 'HOME'
    }
    render(request, 'blog/home.html', data)

