# Generated by Django 4.2.5 on 2024-06-11 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='modified_at',
        ),
        migrations.AddField(
            model_name='date',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
