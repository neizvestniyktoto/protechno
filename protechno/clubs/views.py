from django.shortcuts import render

from .models import Club, Category, Product


def index(request):
    context = {
        "clubs": Club.objects.all(),
        "products": Product.objects.order_by("-amount")
    }
    return render(request, 'base.html', context=context)


"""
Картинка
Товар
Купить
"""