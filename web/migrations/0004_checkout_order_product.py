# Generated by Django 4.2.5 on 2023-10-11 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='order_product',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
