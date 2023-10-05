# Generated by Django 4.2.5 on 2023-10-05 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0015_rename_item_id_cartitem_product_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('added_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('product_price', models.IntegerField(default=0)),
                ('product_image_url', models.CharField(default='', max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
