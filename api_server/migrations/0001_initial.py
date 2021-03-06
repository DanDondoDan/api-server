# Generated by Django 2.1.4 on 2019-01-05 10:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('changed', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('birth', models.DateField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
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
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.CharField(help_text='Forsquare ID of the department.', max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('plural_name', models.CharField(max_length=255, verbose_name='Plural name')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, help_text='Parent department.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='api_server.Department', verbose_name='Parent department')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('changed', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('employment_date', models.DateField(default=None)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='media')),
                ('chief', models.ForeignKey(blank='True', null='True', on_delete=django.db.models.deletion.CASCADE, to='api_server.Person')),
                ('department', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_server.Department')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Person',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('changed', models.DateTimeField(auto_now=True)),
                ('position', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Position',
                'verbose_name_plural': 'Positions',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('changed', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('amount', models.PositiveIntegerField()),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='media/products/')),
                ('category', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_server.Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Product',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='position',
            field=models.ForeignKey(blank='True', null='True', on_delete=django.db.models.deletion.CASCADE, to='api_server.Position'),
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='person', related_query_name='person', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='department',
            unique_together={('parent',)},
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('parent',)},
        ),
    ]
