# Generated by Django 5.0.2 on 2024-04-14 18:44

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
