# Generated by Django 4.2.5 on 2023-09-20 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Category_image',
            new_name='category_image',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='Category_product_no',
            new_name='category_product_no',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='Category_title',
            new_name='category_title',
        ),
    ]