from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
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
    paginate_by = 5

    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Главная страница'
        return ctx


class UserAllNewsView(ListView):
    model = News
    template_name = 'blog/user_news.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(avtor=user).order_by('-date')

    def get_context_data(self, **kwards):
        ctx = super(UserAllNewsView, self).get_context_data(**kwards)

        ctx['title'] = f"Статьи от пользователя {self.kwargs.get('username')}"
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

