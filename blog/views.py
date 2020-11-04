from django.shortcuts import render
from .models import News
from django.views.generic import ListView


class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        ctx = super(ShowNewsView, self).get_context_data(**kwargs)

        ctx['title'] = 'Главная страница'
        return ctx


def contact(request):
    data = {
        'title': 'Страница контакты',
        'contact': 'Контакты'
    }
    return render(request, 'blog/contacti.html', context=data)

