# Generated by Django 3.2.8 on 2021-12-19 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='HELLO!', max_length=200),
        ),
    ]
