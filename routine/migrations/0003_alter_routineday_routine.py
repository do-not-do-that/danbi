# Generated by Django 4.0.5 on 2022-07-05 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0002_alter_routineday_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routineday',
            name='routine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='routine.routine'),
        ),
    ]
