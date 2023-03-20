# Generated by Django 4.1.7 on 2023-03-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtObject', '0002_artstory_borrowed_collection_chariot_other_painting_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artobject',
            name='type',
            field=models.CharField(blank=True, choices=[('CH', 'Chariot'), ('PN', 'Painting'), ('ST', 'Status'), ('HO', 'Holding'), ('OR', 'Other')], max_length=2, null=True),
        ),
    ]