# Generated by Django 3.0.7 on 2020-11-25 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0014_auto_20201121_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='scannedhost',
            name='checked',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]