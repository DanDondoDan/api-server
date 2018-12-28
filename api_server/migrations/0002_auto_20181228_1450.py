# Generated by Django 2.1.4 on 2018-12-28 14:50

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api_server', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(help_text='Forsquare ID of the category.', max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('plural_name', models.CharField(max_length=255, verbose_name='Plural name')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, help_text='Parent category.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='api_server.Category', verbose_name='Parent category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Department', 'verbose_name_plural': 'Departments'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Product'},
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.CharField(help_text='Forsquare ID of the department.', max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='department',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, help_text='Parent department.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='api_server.Department', verbose_name='Parent department'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='media/products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_server.Category'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('parent',)},
        ),
    ]
