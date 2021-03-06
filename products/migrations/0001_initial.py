# Generated by Django 4.0.4 on 2022-05-08 11:59

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
                ('name', models.CharField(max_length=50, verbose_name='Название товара')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('description', models.CharField(blank=True, max_length=150, null=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
            ],
        ),
    ]
