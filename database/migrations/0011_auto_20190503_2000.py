# Generated by Django 2.1.7 on 2019-05-03 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_auto_20190503_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='dms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='oms',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]