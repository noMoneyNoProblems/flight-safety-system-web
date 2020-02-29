# Generated by Django 3.0.3 on 2020-02-28 10:29

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetCommand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('command', models.CharField(choices=[('RTL', 'Return to Launch'), ('HOLD', 'Hold at Current Position'), ('GOTO', 'Goto Position'), ('RON', 'Continue'), ('DISARM', 'Dis-Arm Aircraft'), ('ALT', 'Adjust Altitude'), ('TERM', 'Terminate Flight')], max_length=6)),
                ('position', django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326)),
                ('altitude', models.IntegerField(blank=True, null=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.Asset')),
            ],
        ),
        migrations.AddIndex(
            model_name='assetcommand',
            index=models.Index(fields=['asset', 'timestamp'], name='assets_asse_asset_i_ccd558_idx'),
        ),
    ]
