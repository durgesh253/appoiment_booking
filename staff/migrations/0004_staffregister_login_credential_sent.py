# Generated by Django 5.0 on 2023-12-19 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_alter_staffregister_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffregister',
            name='login_credential_sent',
            field=models.BooleanField(default=False),
        ),
    ]
