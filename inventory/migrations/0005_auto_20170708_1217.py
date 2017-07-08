# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-08 12:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20170708_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('date_created', models.DateField(auto_now=True)),
                ('created_by', models.CharField(default='admin', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'brands',
            },
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_id',
            new_name='barcode',
        ),
        migrations.RemoveField(
            model_name='category',
            name='category_id',
        ),
        migrations.RemoveField(
            model_name='shopcatalogue',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='shopcatalogue',
            name='shop_id',
        ),
        migrations.RemoveField(
            model_name='shopheadquaters',
            name='shop_headquaters_id',
        ),
        migrations.AddField(
            model_name='shopcatalogue',
            name='product',
            field=models.ForeignKey(default='dummy_product', on_delete=django.db.models.deletion.CASCADE, to='inventory.Product', to_field='name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopcatalogue',
            name='shop',
            field=models.ForeignKey(default='dummy_shop', on_delete=django.db.models.deletion.CASCADE, to='inventory.ShopBranch', to_field='name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopcatalogue',
            name='special_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Brand', to_field='name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='shopbranch',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='shopbranch',
            name='parent_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.ShopHeadquaters', to_field='company_name'),
        ),
        migrations.AlterField(
            model_name='shopheadquaters',
            name='company_name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='shopheadquaters',
            name='country',
            field=models.CharField(default='Zimbabwe', max_length=200),
        ),
    ]