# Generated by Django 4.1.5 on 2023-09-25 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_customuser_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(default='', max_length=12),
        ),
    ]
