# Generated by Django 4.1.7 on 2023-03-29 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(choices=[('Scrap Poverty', 'Scrap Poverty'), ('The Way - Addicted to the Mat (Coach Bollinger)', 'The Way - Addicted to the Mat (Coach Bollinger)'), ("The Original Fighter's Voice & Scrap Soldier Collaboration Long Sleeve Shirt", "The Original Fighter's Voice & Scrap Soldier Collaboration Long Sleeve Shirt"), ("The Original Fighter's Voice & Scrap Solider Collaboration Short Sleeve Shirt", "The Original Fighter's Voice & Scrap Solider Collaboration Short Sleeve Shirt"), ("The Original Fighter's Voice & Scrap Soldier Collaboration Pullover Hoodie", "The Original Fighter's Voice & Scrap Soldier Collaboration Pullover Hoodie"), ('North County MMA & Scrap Solider Collaboration Shirt', 'North County MMA & Scrap Solider Collaboration Shirt'), ('Vale Tudo Shorts', 'Vale Tudo Shorts'), ('MMA Shorts (4 Way Stretch)', 'MMA Shorts (4 Way Stretch)'), ('Crop Hoodie For Woman', 'Crop Hoodie For Woman'), ('Star Logo Sticker', 'Star Logo Sticker'), ('Slant T-Shirt (Hottest Selling)', 'Slant T-Shirt (Hottest Selling)'), ('Vertical Flag 1 Color', 'Vertical Flag 1 Color'), ('Military Style Ribbon Hoodie', 'Military Style Ribbon Hoodie')], default='Scrap Poverty', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.CharField(choices=[('The Way', 'https://scrap-soldier-clothing-fight-gear.myshopify.com/products/the-way-addicted-to-the-mat-coach-bollinger'), ('Scrap Poverty', 'https://scrap-soldier-clothing-fight-gear.myshopify.com/products/scrap-poverty'), ('The Way', 'https://scrap-soldier-clothing-fight-gear.myshopify.com/products/the-way-addicted-to-the-mat-coach-bollinger'), ("The Original Fighter's Voice & Scrap Soldier Collaboration Long Sleeve Shirt", 'https://scrap-soldier-clothing-fight-gear.myshopify.com/products/the-original-fighters-voice-scrap-soldier-collaboration-long-sleeve-shirt'), ("The Original Fighter's Voice & Scrap Solider Collaboration Short Sleeve Shirt", 'https://scrap-soldier-clothing-fight-gear.myshopify.com/products/the-original-fighters-voice-and-scrap-solider-collaboration-shirt-short-sleeve'), ("The Original Fighter's Voice & Scrap Soldier Collaboration Pullover Hoodie", 'https://scrap-soldier-clothing-fight-gear.myshopify.com/products/the-original-fighters-voice-scrap-soldier-collaboration-pullover-hoodie'), ('North County MMA & Scrap Solider Collaboration Shirt', 'https://scrap-soldier-clothing-fight-gear.myshopify.com/products/north-county-mma-scrap-solider-collaboration-shirt'), ('Vale Tudo Shorts', 'https://scrap-soldier-clothing-fight-gear.myshopify.com/products/vale-tudo-shorts'), ('MMA Shorts (4 Way Stretch)', 'https://scrap-soldier-clothing-fight-gear.myshopify.com/products/mma-shorts'), ('Crop Hoodie For Woman', 'https://scrap-soldier-clothing-fight-gear.myshopify.com/products/crop-hoodie-for-woman'), ('Star Logo Sticker', 'https://scrap-soldier-clothing-fight-gear.myshopify.com/products/star-sticker'), ('Slant T-Shirt (Hottest Selling)', 'https://scrap-soldier-clothing-fight-gear.myshopify.com/products/slant-t-shirt'), ('Vertical Flag 1 Color', 'https://scrap-soldier-clothing-fight-gear.myshopify.com/products/destroy-your-demons'), ('Military Style Ribbon Hoodie', 'https://scrap-soldier-clothing-fight-gear.myshopify.com/products/military-style-ribbon-hoodie')], max_length=200),
        ),
    ]
