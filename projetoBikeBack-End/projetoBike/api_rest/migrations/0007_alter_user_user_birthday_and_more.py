# Generated by Django 5.1.1 on 2024-10-08 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0006_alter_user_user_birthday_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_birthday',
            field=models.DateField(default='0001-01-01', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_data_validade',
            field=models.DateField(default='0001-01-01', null=True, verbose_name='mm/yyyy'),
        ),
    ]
