# Generated by Django 5.0.6 on 2024-06-10 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(upload_to='social/post_pictures'),
        ),
    ]
