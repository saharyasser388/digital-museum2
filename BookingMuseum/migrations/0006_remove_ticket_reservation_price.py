# Generated by Django 4.1.7 on 2023-03-20 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookingMuseum', '0005_alter_ticket_reservation_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket_reservation',
            name='price',
        ),
    ]
