# Generated by Django 2.1.8 on 2020-08-18 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rendez_vous', '0011_auto_20200818_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rdv',
            name='heure',
            field=models.TimeField(help_text="Veuillez saisir l'heure au format H : M"),
        ),
    ]
