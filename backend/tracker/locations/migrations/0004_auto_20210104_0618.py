# Generated by Django 3.1.3 on 2021-01-04 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_auto_20210104_0611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locations',
            old_name='end_time',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='locations',
            old_name='start_time',
            new_name='start_date',
        ),
    ]
