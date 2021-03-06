# Generated by Django 3.1.5 on 2021-01-26 17:22

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user', verbose_name='User')),
                ('type', models.CharField(choices=[('user', 'User'), ('ambulance_hub', 'Ambulance Hub'), ('ambulance', 'Ambulance')], default='user', max_length=20, verbose_name='Account Type')),
            ],
        ),
        migrations.CreateModel(
            name='AmbulanceHub',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user', verbose_name='User')),
                ('name', models.CharField(max_length=30, verbose_name='Hub Name')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Location')),
            ],
            options={
                'verbose_name': 'Ambulance Hub',
                'verbose_name_plural': 'Ambulance Hubs',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user', verbose_name='User')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('token', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('purpose', models.CharField(choices=[('user_activation', 'User Activation'), ('hub_activation', 'Hub Activation'), ('password_reset', 'Password Reset')], max_length=30, verbose_name='Purpose')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ambulance',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user', verbose_name='User')),
                ('ambulance_no', models.CharField(max_length=30, unique=True, verbose_name='Ambulance Number')),
                ('available', models.BooleanField(verbose_name='Available')),
                ('hub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.ambulancehub')),
            ],
        ),
    ]
