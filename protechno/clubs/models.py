from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Club(models.Model):
    title = models.CharField(max_length=64)
    #image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.title


class Product(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    #image = models.ImageField()

    def __str__(self):
        return self.name



# название
# описание
# категории
# продукция