from django.shortcuts import render
from .models import News
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']

    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Главная страница'
        return ctx


class NewsDetailView(DetailView):
    model = News
    template_name = 'blog/news_detail.html'

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)

        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx


class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text', 'img_article']

    def get_context_data(self, **kwards):
        ctx = super(UpdateNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Обновление статьи'
        ctx['button_text'] = 'Обновить статью'
        ctx['news'] = News.objects.order_by('-date')
        return ctx

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True

        return False

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)


class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text', 'img_article']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwards):
        ctx = super(CreateNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Добавление статьи'
        ctx['button_text'] = 'Добавить статью'
        ctx['news'] = News.objects.order_by('-date')
        return ctx


class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'blog/delete-news.html'

    def get_context_data(self, **kwards):
        ctx = super(DeleteNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Удаление статьи'
        ctx['title_text'] = 'Вы точно хотите удалить статью '
        ctx['button_text_yes'] = 'Да, удалить'
        ctx['button_text_no'] = 'Нет, отмена'
        ctx['news'] = News.objects.order_by('-date')
        return ctx

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True

        return False


def contact(request):
    data = {
        'title': 'Страница контакты',
        'contact': 'Контакты'
    }
    return render(request, 'blog/contacti.html', context=data)

