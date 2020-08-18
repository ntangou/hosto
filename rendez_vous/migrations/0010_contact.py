# Generated by Django 2.1.8 on 2020-08-11 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rendez_vous', '0009_auto_20200810_0141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('sujet', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]