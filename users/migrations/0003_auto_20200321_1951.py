# Generated by Django 3.0.4 on 2020-03-21 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200321_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(default='tento člověk nám o sobě absolutně nic neřekl, nevěřte mu', max_length=200),
        ),
    ]
