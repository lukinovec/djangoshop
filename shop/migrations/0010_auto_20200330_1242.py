# Generated by Django 3.0.4 on 2020-03-30 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200330_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='about',
            field=models.TextField(default='sample text', max_length=400),
        ),
        migrations.AlterField(
            model_name='item',
            name='original',
            field=models.CharField(max_length=200),
        ),
    ]
