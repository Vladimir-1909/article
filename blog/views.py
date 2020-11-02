from django.shortcuts import render


def home(request):
    news = [
        {
            'title': 'Наша первая статья',
            'text': 'Полный текст статьи',
            'date': '1 января 2020 года',
            'avtor': 'Джон'
        },
        {
            'title': 'Наша вторая статья',
            'text': 'Полный текст статьи',
            'date': '2 января 2020 года',

        }
    ]

    data = {
        'title': 'Главная страница',
        'news': news
    }
    return render(request, 'blog/home.html', data)


def contact(request):
    data = {
        'title': 'Страница контакты',
        'contact': 'Контакты'
    }
    return render(request, 'blog/contacti.html', context=data)

