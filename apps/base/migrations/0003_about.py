# Generated by Django 4.2.7 on 2023-11-20 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_slide'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.TextField(verbose_name='Описание о нас')),
            ],
            options={
                'verbose_name': ('О нас',),
                'verbose_name_plural': 'О нас',
            },
        ),
    ]
