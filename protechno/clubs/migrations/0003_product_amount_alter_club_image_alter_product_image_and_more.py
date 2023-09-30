# Generated by Django 4.2.5 on 2023-09-30 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_remove_club_category_club_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='club',
            name='image',
            field=models.FileField(default='', upload_to='static/uploads/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(default='', upload_to='static/uploads/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]