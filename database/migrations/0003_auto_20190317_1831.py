# Generated by Django 2.1.7 on 2019-03-17 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20190315_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='description',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='description',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='mail',
        ),
    ]
