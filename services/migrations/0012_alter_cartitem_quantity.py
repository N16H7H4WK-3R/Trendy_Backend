# Generated by Django 4.1.5 on 2023-09-30 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_cartitem_delete_cart_delete_itemincart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]