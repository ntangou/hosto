# Generated by Django 2.1.8 on 2020-08-09 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rendez_vous', '0007_auto_20200808_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Siteweb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('qr_code', models.ImageField(blank=True, upload_to='qr_codes')),
            ],
        ),
    ]