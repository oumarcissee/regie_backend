# Generated by Django 4.2.5 on 2024-06-11 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_date_modified_at_date_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderArchives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('ref', models.CharField(max_length=50, unique=True)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='date_archiv', to='app.date')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_archiv', to='app.order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
