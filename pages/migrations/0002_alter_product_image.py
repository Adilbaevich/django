# Generated by Django 4.1.6 on 2023-07-06 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='media/%Y/%m/%d/'),
        ),
    ]