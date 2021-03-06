# Generated by Django 2.1.8 on 2020-08-06 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20200806_0041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_personnel', models.ImageField(upload_to='')),
                ('nom', models.CharField(max_length=150)),
                ('prenom', models.CharField(blank=True, max_length=150)),
                ('sexe', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1)),
                ('email', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('tweeter', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Service')),
                ('titre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Titre')),
            ],
        ),
    ]
