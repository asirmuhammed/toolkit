# Generated by Django 4.2.5 on 2023-09-20 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_rename_category_image_category_category_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_del_price',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]