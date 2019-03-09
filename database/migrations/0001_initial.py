# Generated by Django 2.1.7 on 2019-03-09 10:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('symptoms', models.TextField(default=None, max_length=1000)),
            ],
            options={
                'verbose_name': 'Disease',
                'verbose_name_plural': 'Diseases',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('dateOfBirthday', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=None, max_length=1, verbose_name='gender')),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('city', models.CharField(default=None, max_length=45)),
                ('mail', models.CharField(default=None, max_length=100)),
                ('password', models.CharField(default=None, max_length=30)),
                ('phone_number', models.IntegerField(null=True)),
                ('name_of_organisation', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctors',
            },
        ),
        migrations.CreateModel(
            name='DoctorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('diseases', models.ManyToManyField(to='database.Disease')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimony', models.IntegerField()),
                ('comment', models.TextField(default=None)),
                ('date', models.DateTimeField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Indicator')),
            ],
        ),
        migrations.CreateModel(
            name='MeasurementFrequency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicator', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='database.Indicator')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(choices=[('D', 'Doctor'), ('P', 'Patient')], default=None, max_length=1, verbose_name='Author')),
                ('message', models.TextField(default=None)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='database.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('dateOfBirthday', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=None, max_length=1, verbose_name='gender')),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('city', models.CharField(default=None, max_length=45)),
                ('mail', models.CharField(default=None, max_length=100)),
                ('password', models.CharField(default=None, max_length=30)),
                ('phone_number', models.IntegerField(null=True)),
                ('diseases', models.ManyToManyField(to='database.Disease')),
                ('doctors', models.ManyToManyField(to='database.Doctor')),
            ],
            options={
                'verbose_name': 'Patient',
                'verbose_name_plural': 'Patients',
            },
        ),
        migrations.AddField(
            model_name='message',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='database.Patient'),
        ),
        migrations.AddField(
            model_name='measurementfrequency',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='database.Patient'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.DoctorType'),
        ),
        migrations.AddField(
            model_name='disease',
            name='doctorType',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='database.DoctorType'),
        ),
    ]
