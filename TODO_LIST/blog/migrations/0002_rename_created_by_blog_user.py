# Generated by Django 5.1.6 on 2025-03-01 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='created_by',
            new_name='user',
        ),
    ]
