# Generated by Django 3.2.8 on 2021-10-23 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='categoria'),
        ),
    ]
