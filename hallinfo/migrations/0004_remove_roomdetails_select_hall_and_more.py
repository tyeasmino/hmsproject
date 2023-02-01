# Generated by Django 4.1.5 on 2023-01-30 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hallinfo', '0003_roomdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomdetails',
            name='select_hall',
        ),
        migrations.AlterField(
            model_name='roomdetails',
            name='select_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hallinfo.roominfo'),
        ),
    ]