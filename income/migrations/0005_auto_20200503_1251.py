# Generated by Django 3.0.3 on 2020-05-03 12:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0004_auto_20200419_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='income',
            name='description',
            field=models.TextField(default='_'),
        ),
    ]
