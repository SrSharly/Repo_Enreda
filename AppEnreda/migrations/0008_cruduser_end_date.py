# Generated by Django 2.0.13 on 2019-08-25 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEnreda', '0007_auto_20190825_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='cruduser',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
