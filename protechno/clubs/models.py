from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=32, default='')

    def __str__(self):
        return self.title


class Club(models.Model):
    title = models.CharField(max_length=64, default='')
    image = models.FileField(upload_to='static/uploads/', default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    is_service = models.BooleanField(default=False)
    image = models.FileField(upload_to='static/uploads/', default='')

    def __str__(self):
        return self.name
