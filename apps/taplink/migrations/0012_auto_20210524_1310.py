# Generated by Django 3.1.7 on 2021-05-24 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taplink', '0011_auto_20210524_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taplink',
            name='slug',
            field=models.SlugField(blank=True, default=None, verbose_name='Ссылка'),
        ),
    ]