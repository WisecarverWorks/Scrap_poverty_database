# Generated by Django 4.1.7 on 2023-03-29 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(choices=[(3.0, 3.0), (15.0, 15.0), (20.0, 20.0), (22.5, 22.5), (25.0, 25.0), (27.5, 27.5), (29.0, 29.0), (29.95, 29.95), (32.5, 32.5), (35.0, 35.0), (39.95, 39.95)], max_length=5),
        ),
    ]
