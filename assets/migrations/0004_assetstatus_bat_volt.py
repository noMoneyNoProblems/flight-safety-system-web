# Generated by Django 3.2.6 on 2021-11-27 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20200912_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetstatus',
            name='bat_volt',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]
