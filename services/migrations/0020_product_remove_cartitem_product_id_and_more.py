# Generated by Django 4.2.5 on 2023-10-05 15:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0019_alter_customuser_country_alter_customuser_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=500)),
                ('price', models.IntegerField(default=0)),
                ('image_url', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product_image_url',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product_price',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product_title',
        ),
        migrations.RemoveField(
            model_name='favoriteitem',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='favoriteitem',
            name='product_image_url',
        ),
        migrations.RemoveField(
            model_name='favoriteitem',
            name='product_price',
        ),
        migrations.RemoveField(
            model_name='favoriteitem',
            name='product_title',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='country',
            field=models.CharField(default='INDIA', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.localtime, editable=False),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='services.product'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='cart_items',
            field=models.ManyToManyField(blank=True, related_name='users_cart', through='services.CartItem', to='services.product'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='favorite_items',
            field=models.ManyToManyField(blank=True, related_name='users_favorite', through='services.FavoriteItem', to='services.product'),
        ),
        migrations.AddField(
            model_name='favoriteitem',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='services.product'),
        ),
    ]
