# Generated by Django 4.1.7 on 2023-02-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_rename_image_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]