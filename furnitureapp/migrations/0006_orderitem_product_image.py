# Generated by Django 5.0.1 on 2024-02-09 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitureapp', '0005_remove_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='product_image',
            field=models.URLField(null=True),
        ),
    ]
