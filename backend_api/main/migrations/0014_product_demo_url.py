# Generated by Django 4.2.4 on 2023-09-23 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_product_tags_product_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='demo_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]