# Generated by Django 5.1 on 2024-09-30 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_timeline_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeline',
            name='description',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
