# Generated by Django 4.0.6 on 2022-07-21 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', models.CharField(max_length=60, verbose_name='collection')),
                ('title', models.CharField(max_length=65, verbose_name='title')),
                ('description', models.CharField(max_length=100, verbose_name='description')),
                ('image', models.ImageField(upload_to='banners/', verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('is_active', models.BooleanField(blank=True, default=False, verbose_name='is active')),
            ],
            options={
                'verbose_name': 'banner',
                'verbose_name_plural': 'banners',
            },
        ),
    ]
