# Generated by Django 4.1.7 on 2023-02-24 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=1000, verbose_name='Название продукта')),
                ('description', models.TextField(max_length=10000, null=True, verbose_name='Описание')),
                ('image', models.TextField(max_length=10000, verbose_name='Ссылка изображения')),
                ('category', models.TextField(default='Other', max_length=500, verbose_name='Категория')),
                ('remain', models.IntegerField(verbose_name='Остаток')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
            ],
        ),
    ]
