# Generated by Django 2.1.8 on 2020-08-05 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('nom_service', models.CharField(max_length=50)),
                ('specialiteM', models.CharField(max_length=50)),
                ('specialiteF', models.CharField(max_length=50)),
                ('contenu', models.TextField()),
            ],
        ),
    ]
