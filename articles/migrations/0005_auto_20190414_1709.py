# Generated by Django 2.2 on 2019-04-14 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20190414_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=150, null=True, verbose_name='Autor'),
        ),
    ]
