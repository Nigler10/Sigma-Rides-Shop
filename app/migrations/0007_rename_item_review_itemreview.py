# Generated by Django 4.2.16 on 2025-01-22 06:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_item_review'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item_Review',
            new_name='ItemReview',
        ),
    ]
