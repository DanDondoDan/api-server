# Generated by Django 2.1.4 on 2019-01-09 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_server', '0010_auto_20190109_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True, help_text='Is this product publicly visible.'),
        ),
    ]