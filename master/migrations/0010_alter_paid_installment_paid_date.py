# Generated by Django 5.0.1 on 2024-01-10 08:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0009_alter_paid_installment_paid_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paid_installment',
            name='paid_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 10, 8, 47, 31, 914156, tzinfo=datetime.timezone.utc)),
        ),
    ]
