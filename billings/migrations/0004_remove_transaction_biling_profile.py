# Generated by Django 3.0.8 on 2020-07-26 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billings', '0003_auto_20200726_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='biling_profile',
        ),
    ]
