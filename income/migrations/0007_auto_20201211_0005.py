# Generated by Django 3.1.4 on 2020-12-10 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0006_auto_20200517_0528'),
    ]

    operations = [
        migrations.RenameField(
            model_name='income',
            old_name='income_date',
            new_name='date',
        ),
    ]
