# Generated by Django 3.1.6 on 2021-05-06 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0012_auto_20210506_0227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vulnerability',
            old_name='host',
            new_name='subdomain',
        ),
    ]