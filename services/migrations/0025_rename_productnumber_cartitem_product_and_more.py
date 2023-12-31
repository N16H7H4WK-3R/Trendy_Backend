# Generated by Django 4.2.5 on 2023-10-06 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0024_rename_product_cartitem_productnumber_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='productNumber',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='product',
            name='productNumber',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
