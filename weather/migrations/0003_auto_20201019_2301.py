# Generated by Django 2.1.5 on 2020-10-19 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_auto_20201019_2300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'cities'},
        ),
    ]
