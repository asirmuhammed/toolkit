# Generated by Django 4.2.5 on 2023-09-18 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_remove_blog_summary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='ppoi',
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
