from django.contrib import admin
from django.core.files.base import ContentFile

from .models import Club, Product, Category
from PIL import Image

import io
import os.path

from django.conf import settings
from django.core.files.base import ContentFile
from django.db import models
from django.db.models.fields.files import ImageFieldFile

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    fields = ['title', 'image_webp',  'description']
    """
    def save_model(self, request, obj, form, change):
        user = request.user
        instance = form.save(commit=False)
        instance.image.seek(0)
        image = Image.open(instance.image)
        image_bytes = io.BytesIO()
        print(image_bytes)
        image.save(fp=image_bytes, format="WEBP")
        print(os.path.splitext(instance.image.url)[0] + '.webp')
        instance.image_webp.save(os.path.splitext(instance.image.url)[0] + '.webp',
                                 content=image_bytes.getvalue())
        print(instance.image_webp.url)
        instance.save()
        form.save_m2m()
        return instance
    """

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'image_webp', 'image',  'amount',  'price', 'category', 'is_service']

#admin.site.register(Club)
#admin.site.register(Product)
admin.site.register(Category)

# сувениры - souvenirs
# мебедь - furniture
# гончарка - pottery