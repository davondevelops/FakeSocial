# Generated by Django 2.2.4 on 2020-12-18 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201218_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='likes',
            field=models.ManyToManyField(related_name='liked_quotes', to='app.User'),
        ),
    ]
