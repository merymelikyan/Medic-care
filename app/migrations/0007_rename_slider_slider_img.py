# Generated by Django 5.1 on 2024-09-28 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_slider_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='slider',
            new_name='img',
        ),
    ]
