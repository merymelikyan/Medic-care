# Generated by Django 5.1.1 on 2024-09-25 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='footertext',
            name='link_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
