# Generated by Django 4.0.6 on 2022-07-20 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='image',
            field=models.FilePathField(default='img/default.jpeg', path='/img'),
            preserve_default=False,
        ),
    ]
