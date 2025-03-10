# Generated by Django 5.1.1 on 2024-09-07 20:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='token',
            field=models.CharField(default=uuid.uuid4, max_length=255, unique=True, verbose_name='User auth token'),
        ),
    ]
