# Generated by Django 4.1.7 on 2023-02-24 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='selected_yn',
            field=models.BooleanField(default=False),
        ),
    ]
