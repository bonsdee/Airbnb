# Generated by Django 5.1.7 on 2025-03-22 09:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('booking_status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], max_length=50)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.guest')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('Credit Card', 'Credit Card'), ('PayPal', 'PayPal'), ('Bank Transfer', 'Bank Transfer')], max_length=50)),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')], max_length=50)),
                ('transaction_date', models.DateField()),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.booking')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.guest')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.TextField()),
                ('description', models.TextField()),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.owner')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.property'),
        ),
    ]
