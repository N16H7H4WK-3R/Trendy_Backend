# Generated by Django 5.0.1 on 2024-02-01 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0003_alter_user_options_remove_user_created_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'Users'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='user',
            name='modified_by',
        ),
    ]
