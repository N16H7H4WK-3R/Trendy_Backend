# Generated by Django 5.0.1 on 2024-01-25 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_managers_customuser_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('admin', 'Admin'), ('user', 'User'), ('seller', 'Seller')], default='user', max_length=20),
        ),
    ]