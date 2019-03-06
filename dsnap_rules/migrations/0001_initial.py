# Generated by Django 2.1.7 on 2019-02-21 03:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'db_table': 'application_period',
            },
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'county',
            },
        ),
        migrations.CreateModel(
            name='Disaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disaster_request_no', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('benefit_begin_date', models.DateField()),
                ('benefit_end_date', models.DateField()),
                ('residency_required', models.BooleanField()),
                ('uses_DSED', models.BooleanField()),
                ('allows_food_loss_alone', models.BooleanField()),
            ],
            options={
                'db_table': 'disaster',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('abbreviation', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'state',
            },
        ),
        migrations.AddField(
            model_name='disaster',
            name='state',
            field=models.ForeignKey(db_column='state', on_delete=django.db.models.deletion.CASCADE, related_name='disasters', to='dsnap_rules.State'),
        ),
        migrations.AddField(
            model_name='county',
            name='state',
            field=models.ForeignKey(db_column='state', on_delete=django.db.models.deletion.CASCADE, related_name='counties', to='dsnap_rules.State'),
        ),
        migrations.AddField(
            model_name='applicationperiod',
            name='counties',
            field=models.ManyToManyField(to='dsnap_rules.County'),
        ),
        migrations.AddField(
            model_name='applicationperiod',
            name='disaster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_periods', to='dsnap_rules.Disaster'),
        ),
    ]
