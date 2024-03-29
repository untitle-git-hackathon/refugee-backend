# Generated by Django 2.2.3 on 2019-07-06 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Refugee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='refugee.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('is_from_refugee', models.BooleanField()),
                ('image_url', models.TextField(blank=True)),
                ('refugee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='refugee.Refugee')),
            ],
        ),
        migrations.CreateModel(
            name='Qa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_answer_image', models.CharField(max_length=30)),
                ('wrong_answer_image', models.CharField(max_length=30)),
                ('story', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='refugee.Story')),
            ],
        ),
    ]
