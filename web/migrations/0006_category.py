# Generated by Django 4.2.5 on 2023-09-20 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_image', models.ImageField(upload_to='')),
                ('Category_title', models.CharField(max_length=30)),
                ('Category_product_no', models.CharField(max_length=30)),
            ],
        ),
    ]
