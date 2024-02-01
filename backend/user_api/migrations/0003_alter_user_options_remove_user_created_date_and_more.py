# Generated by Django 5.0.1 on 2024-02-01 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0002_user_is_staff_alter_user_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'All users'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='created_date',
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Admin'), (2, 'Seller'), (3, 'Customer')], default=3, null=True),
        ),
    ]