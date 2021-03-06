# Generated by Django 2.0.2 on 2018-03-02 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20180302_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogParent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='catalog',
            name='parent',
        ),
        migrations.AddField(
            model_name='catalogparent',
            name='child',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_category_fk', to='shop.Catalog'),
        ),
        migrations.AddField(
            model_name='catalogparent',
            name='parent',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent_category_fk', to='shop.Catalog'),
        ),
    ]
