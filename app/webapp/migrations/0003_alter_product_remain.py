# Generated by Django 4.1.7 on 2023-02-24 18:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_product_remain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='remain',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Остаток'),
        ),
    ]
