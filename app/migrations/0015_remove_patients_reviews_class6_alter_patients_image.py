# Generated by Django 5.1 on 2024-10-02 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_rename_description_ourclinic_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patients',
            name='reviews_class6',
        ),
        migrations.AlterField(
            model_name='patients',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='patients'),
        ),
    ]
