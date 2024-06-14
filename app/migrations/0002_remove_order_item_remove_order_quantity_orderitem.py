# Generated by Django 4.2.5 on 2024-05-14 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('ref', models.CharField(max_length=50, unique=True)),
                ('quantity', models.IntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_order', to='app.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderItem', to='app.order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]