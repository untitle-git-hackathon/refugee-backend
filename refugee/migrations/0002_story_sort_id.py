# Generated by Django 2.2.3 on 2019-07-07 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refugee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='sort_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]