# Generated by Django 3.2.12 on 2023-05-16 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalog_dish', models.CharField(max_length=30, verbose_name='Dish Name: ')),
                ('catalog_price', models.IntegerField(verbose_name='Dish Price: ')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=30, verbose_name='Customer Full Name: ')),
                ('customer_spendings', models.IntegerField(verbose_name='Customer Spendings: ')),
                ('customer_premium', models.BooleanField(default=0, max_length=30, verbose_name='Customer Premium: ')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_type', models.CharField(default='', max_length=30, verbose_name='Order Type: ')),
            ],
        ),
    ]
