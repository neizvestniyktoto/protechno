from django.db import models

from django_resized import ResizedImageField


class Category(models.Model):
    title = models.CharField(max_length=32, default='')

    def __str__(self):
        return self.title


class Club(models.Model):
    title = models.CharField(max_length=64, default='')
    image = models.ImageField(upload_to='static/uploads/src', default='')
    image_webp = ResizedImageField(force_format="WEBP", upload_to='static/uploads/src', default='', quality=100)
    description = models.TextField(default='')

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    is_service = models.BooleanField(default=False)
    image = models.FileField(upload_to='static/uploads/src', default='#')
    image_webp = ResizedImageField(force_format="WEBP", upload_to='static/uploads/src', default='', quality=100)

    def __str__(self):
        return self.name
