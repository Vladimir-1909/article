from django.contrib import admin
from django.urls import path
from django.urls import include
from users import views as userViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('reg/', userViews.register, name='reg'),
]
