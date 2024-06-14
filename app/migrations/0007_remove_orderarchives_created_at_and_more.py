# Generated by Django 4.2.5 on 2024-06-12 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_orderarchives'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderarchives',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='orderarchives',
            name='modified_at',
        ),
        migrations.RemoveField(
            model_name='orderarchives',
            name='ref',
        ),
        migrations.AddField(
            model_name='date',
            name='days',
            field=models.IntegerField(default=0),
        ),
    ]
