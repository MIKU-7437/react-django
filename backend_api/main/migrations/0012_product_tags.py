# Generated by Django 4.2.4 on 2023-09-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_productcategory_slug_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.TextField(null=True),
        ),
    ]
