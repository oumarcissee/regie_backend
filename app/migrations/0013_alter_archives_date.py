# Generated by Django 4.2.5 on 2024-06-21 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_archives_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archives',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
