# Generated by Django 5.1 on 2024-09-02 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of creating')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date of updating')),
                ('phone', models.CharField(max_length=20, unique=True, verbose_name='Phone number')),
                ('token', models.CharField(max_length=255, unique=True, verbose_name='User auth token')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
    ]
