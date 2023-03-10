# Generated by Django 4.1.5 on 2023-01-30 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HallInfo',
            fields=[
                ('hall_pk', models.AutoField(primary_key=True, serialize=False)),
                ('hall_id', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('residence_type', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE')], default='Male', max_length=10)),
                ('hall_launch_date', models.DateField()),
                ('temp_pass', models.CharField(default='hmsprovost', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RoomInfo',
            fields=[
                ('room_pk', models.AutoField(primary_key=True, serialize=False)),
                ('room_no', models.CharField(max_length=20, unique=True)),
                ('room_capacity', models.IntegerField()),
                ('room_allotment', models.IntegerField()),
                ('room_empty', models.IntegerField()),
                ('comment', models.CharField(blank=True, max_length=200)),
                ('hall_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hallinfo.hallinfo')),
            ],
        ),
    ]
