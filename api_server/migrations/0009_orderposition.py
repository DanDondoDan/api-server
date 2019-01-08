# Generated by Django 2.1.4 on 2019-01-08 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_server', '0008_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_server.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_server.Product')),
            ],
            options={
                'verbose_name': 'Order position',
                'verbose_name_plural': 'Order Positions',
                'ordering': ['-count'],
            },
        ),
    ]