# Generated by Django 3.0.4 on 2020-03-29 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.CharField(default='https://lh3.googleusercontent.com/yVQO8bmGhYjQHYATrXQeaswpZawKBWuiSx1vd4skj2TLMT-JGj8WfPiYFSiULKt0Pg420-zMy_BK7EXV4OTk=s400', max_length=300),
        ),
    ]