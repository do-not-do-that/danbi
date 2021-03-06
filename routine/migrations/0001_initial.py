# Generated by Django 4.0.5 on 2022-07-05 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('MI', 'MIRACLE'), ('HOMEWORK', 'HOMEWORK')], default='MI', max_length=8)),
                ('goal', models.CharField(blank=True, max_length=500, null=True)),
                ('is_alarm', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'routine',
            },
        ),
        migrations.CreateModel(
            name='RoutineResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(choices=[('N', 'NOT'), ('T', 'TRY'), ('D', 'DONE')], default='N', max_length=4)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('routine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routine.routine')),
            ],
            options={
                'db_table': 'routine_result',
            },
        ),
        migrations.CreateModel(
            name='RoutineDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', multiselectfield.db.fields.MultiSelectField(choices=[('MON', 'MON'), ('TUE', 'TUE'), ('WED', 'WED'), ('THU', 'THU'), ('FRI', 'FRI'), ('SAT', 'SAT'), ('SUN', 'SUN')], max_length=27)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('routine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routine.routine')),
            ],
            options={
                'db_table': 'routine_day',
            },
        ),
    ]
