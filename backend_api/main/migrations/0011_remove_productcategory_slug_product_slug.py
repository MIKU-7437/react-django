# Generated by Django 4.2.4 on 2023-09-17 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_productcategory_slug_alter_productimage_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='slug',
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
