# Generated by Django 4.1.7 on 2023-03-20 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookingMuseum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket_reservation',
            name='type',
            field=models.CharField(blank=True, choices=[('Egyptian_Citizen', 'Egyptian_Citizen'), ('Egyptian_Student', 'Egyptian_Student'), ('Foreign_Visitor', 'Foreign_Visitor'), ('Foreign_Student', 'Foreign_Student'), ('photographic_camera', 'photographic_camera')], max_length=255, null=True),
        ),
    ]
