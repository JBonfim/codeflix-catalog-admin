# Generated by Django 5.1.4 on 2024-12-06 20:58

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
    ]
