# Generated by Django 2.0.13 on 2019-08-23 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEnreda', '0002_auto_20190823_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='cruduser',
            name='user',
            field=models.ManyToManyField(to='AppEnreda.Creador'),
        ),
    ]