# Generated by Django 4.2.5 on 2024-06-12 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_orderarchives_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='date',
            old_name='days',
            new_name='nomber_of_days',
        ),
    ]
