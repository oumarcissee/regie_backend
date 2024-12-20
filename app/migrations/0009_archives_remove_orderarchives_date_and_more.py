# Generated by Django 4.2.5 on 2024-06-12 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_days_date_nomber_of_days'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('nomber_of_days', models.IntegerField(default=0)),
                ('discharge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discharge_archiv', to='app.discharge')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_archiv', to='app.order')),
            ],
        ),
        migrations.RemoveField(
            model_name='orderarchives',
            name='date',
        ),
        migrations.RemoveField(
            model_name='orderarchives',
            name='order',
        ),
        migrations.DeleteModel(
            name='Date',
        ),
        migrations.DeleteModel(
            name='OrderArchives',
        ),
    ]
