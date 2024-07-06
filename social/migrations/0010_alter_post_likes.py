# Generated by Django 5.0.6 on 2024-06-10 11:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("social", "0009_alter_post_picture"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="likes", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
