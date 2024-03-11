# Generated by Django 5.0.1 on 2024-03-11 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='poets',
            fields=[
                ('poet_id', models.IntegerField(primary_key=True, serialize=False)),
                ('poet_cat', models.CharField(max_length=255)),
                ('poet_link', models.URLField(max_length=255)),
                ('poet_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Poems',
            fields=[
                ('poem_id', models.IntegerField(primary_key=True, serialize=False)),
                ('poem_link', models.URLField(max_length=255)),
                ('poem_style', models.CharField(max_length=255)),
                ('poem_text', models.TextField()),
                ('poem_title', models.CharField(max_length=255)),
                ('poet_cat', models.CharField(max_length=255)),
                ('poet_link', models.URLField(max_length=255)),
                ('poet_name', models.CharField(max_length=255)),
                ('poet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.poets')),
            ],
        ),
    ]
