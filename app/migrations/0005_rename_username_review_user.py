# Generated by Django 4.2.16 on 2025-01-29 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_user_review_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='username',
            new_name='user',
        ),
    ]
