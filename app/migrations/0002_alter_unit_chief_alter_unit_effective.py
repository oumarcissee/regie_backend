# Generated by Django 4.2.5 on 2023-12-16 06:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="unit",
            name="chief",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="unit",
            name="effective",
            field=models.IntegerField(default=1),
        ),
    ]
