from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img_profile = models.ImageField('Фото пользователя', default='default-plofile.png', upload_to='img_user')

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'
