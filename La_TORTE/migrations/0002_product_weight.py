# Generated by Django 3.2.8 on 2021-10-24 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('La_TORTE', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.PositiveSmallIntegerField(default=1000, verbose_name='Вес'),
        ),
    ]
