# Generated by Django 3.1.3 on 2021-01-04 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_auto_20210104_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]
