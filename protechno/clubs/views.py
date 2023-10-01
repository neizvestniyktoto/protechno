from django.shortcuts import render

from .models import Club, Product


def index(request):
    context = {
        "clubs": Club.objects.all(),
        "products": Product.objects.order_by("-amount")
    }
    return render(request, 'home.html', context=context)
