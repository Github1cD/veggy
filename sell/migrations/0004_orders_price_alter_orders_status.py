# Generated by Django 4.1.5 on 2023-01-27 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0003_orders_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('ordered', 'ordered'), ('confirmed', 'confirm'), ('delivered', 'deliver'), ('canceled', 'cancel')], default='ordered', max_length=10),
        ),
    ]
