from django.shortcuts import render
from django.shortcuts import redirect
from blog.models import News
from .forms import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан!')
            return redirect('home')
    else:
        form = UserRegisterForm()

    data = {
        'title': 'Страница регистрации',
        'title_form': 'Регистрация',
        'news': News.objects.all(),
        'form': form
    }
    return render(request, 'users/registertration.html', context=data)
