# Generated by Django 4.0.8 on 2023-06-14 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketcourses', '0006_alter_product_image_alter_product_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='marketcourses/static/marketcourses/img'),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='marketcourses/static/marketcourses/img'),
        ),
    ]
