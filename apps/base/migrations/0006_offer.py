# Generated by Django 4.2.7 on 2023-11-20 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_history_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='offer_image', verbose_name='Фотография')),
                ('title', models.CharField(max_length=255, verbose_name='Название блюда')),
                ('descriptions', models.TextField(verbose_name='Описание блюда')),
                ('price', models.CharField(max_length=255, verbose_name='Цена')),
                ('type', models.CharField(max_length=255, verbose_name='Тип блюда')),
            ],
            options={
                'verbose_name': ('Предложение',),
                'verbose_name_plural': 'Предложение',
            },
        ),
    ]
