# Generated by Django 2.1.7 on 2019-04-23 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_auto_20190423_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.Patient'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.Indicator'),
        ),
    ]