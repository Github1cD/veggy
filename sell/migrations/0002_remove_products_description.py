# Generated by Django 4.1.4 on 2023-01-09 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='description',
        ),
    ]
