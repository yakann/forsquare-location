# Generated by Django 4.0.3 on 2022-12-04 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forsquare_api', '0002_alter_location_latitude_alter_location_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='fsq_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='region',
            field=models.CharField(max_length=200, null=True),
        ),
    ]