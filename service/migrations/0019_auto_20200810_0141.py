# Generated by Django 2.1.8 on 2020-08-10 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0018_auto_20200809_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Service'),
        ),
    ]
