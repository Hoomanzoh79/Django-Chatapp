# Generated by Django 5.0.6 on 2024-06-01 07:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_bio_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(regex='^[0][9][0-9][0-9]{8,8}$')]),
        ),
    ]