# Generated by Django 2.0.2 on 2018-03-02 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20180302_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttocatalog',
            name='catalog',
        ),
        migrations.RemoveField(
            model_name='producttocatalog',
            name='product',
        ),
        migrations.DeleteModel(
            name='Catalog',
        ),
        migrations.DeleteModel(
            name='ProductToCatalog',
        ),
    ]
