# Generated by Django 3.1.5 on 2021-02-05 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0003_auto_20210206_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
