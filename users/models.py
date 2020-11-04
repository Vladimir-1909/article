from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img_profile = models.ImageField('Фото пользователя', default='default-plofile.png', upload_to='img_user')

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img_profile.path)

        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img_profile.path)

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'
