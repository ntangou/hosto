# Generated by Django 2.1.8 on 2020-08-06 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Heure',
            fields=[
                ('heure', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Rdv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_personnel', models.CharField(max_length=150)),
                ('prenom_personnel', models.CharField(blank=True, max_length=150)),
                ('date', models.DateTimeField()),
                ('heure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rendez_vous.Heure')),
            ],
        ),
    ]
