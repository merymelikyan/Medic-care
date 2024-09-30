# Generated by Django 5.1 on 2024-09-28 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_footertext_link_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slaider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slide1', models.ImageField(upload_to='header_text')),
            ],
            options={
                'verbose_name': 'Header Text',
                'verbose_name_plural': 'Header Text',
            },
        ),
        migrations.RemoveField(
            model_name='headertext',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='headertext',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='headertext',
            name='image3',
        ),
    ]
