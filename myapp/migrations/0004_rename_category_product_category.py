# Generated by Django 4.2.4 on 2023-08-18 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_product_category_product_vendor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Category',
            new_name='category',
        ),
    ]
