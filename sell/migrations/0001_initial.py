# Generated by Django 4.0.6 on 2022-12-28 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=40)),
                ('product_image', models.ImageField(default='products/dummy.jpg', upload_to='products/')),
                ('description', models.CharField(default='description not available', max_length=500)),
                ('total_quantity', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.user_details')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sell.products')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.user_details')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
