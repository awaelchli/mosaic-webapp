# Generated by Django 2.2.5 on 2019-09-14 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosaic', '0004_auto_20190914_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mosaic',
            name='uploaded_file',
            field=models.ImageField(upload_to='inputs/', verbose_name='File'),
        ),
    ]
