# Generated by Django 3.1.3 on 2020-11-11 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workhours', '0003_auto_20201111_1805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workhours',
            old_name='day',
            new_name='day_end',
        ),
        migrations.AddField(
            model_name='workhours',
            name='day_start',
            field=models.CharField(choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday'), ('SU', 'Sunday')], default='MO', max_length=2, verbose_name='Day'),
        ),
    ]