# Generated by Django 4.2.5 on 2023-10-06 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0020_product_remove_cartitem_product_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='imageUrl',
            field=models.URLField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='product',
            name='imageUrl1',
            field=models.URLField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='product',
            name='imageUrl2',
            field=models.URLField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='product',
            name='imageUrl3',
            field=models.URLField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='product',
            name='productDescription',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='productId',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='product',
            name='productPrice',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='product',
            name='productTitle',
            field=models.CharField(default='', max_length=255),
        ),
    ]
