# Generated by Django 5.1.1 on 2024-09-25 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimatedInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
                ('title1', models.CharField(blank=True, max_length=255, null=True)),
                ('title2', models.CharField(blank=True, max_length=255, null=True)),
                ('title3', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(max_length=250)),
                ('phone', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'verbose_name': 'AnimatedInfo',
                'verbose_name_plural': 'AnimatedInfo',
            },
        ),
        migrations.CreateModel(
            name='FooterText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.CharField(blank=True, max_length=255, null=True)),
                ('text2', models.CharField(blank=True, max_length=255, null=True)),
                ('text3', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Footer Text',
                'verbose_name_plural': 'Footer Text',
            },
        ),
        migrations.CreateModel(
            name='HeaderText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(max_length=255)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='courses')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='courses')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='courses')),
            ],
            options={
                'verbose_name': 'Header Text',
                'verbose_name_plural': 'Header Text',
            },
        ),
    ]
