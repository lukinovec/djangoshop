# Generated by Django 3.0.4 on 2020-04-06 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200406_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(default="Popisek profilu můžete <a href='{% url 'profile' %}'>změnit</a>", max_length=200),
        ),
    ]
