# Generated by Django 3.0.7 on 2020-11-03 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_news_img_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='img_article',
            field=models.ImageField(default='default-article.jpg', upload_to='img_article', verbose_name='Фото статьи'),
        ),
    ]
