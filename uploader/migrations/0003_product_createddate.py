# Generated by Django 4.2 on 2023-12-20 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0002_remove_product_navn'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='CreatedDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]