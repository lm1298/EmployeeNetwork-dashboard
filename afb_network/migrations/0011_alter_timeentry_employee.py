# Generated by Django 5.0.2 on 2024-07-29 20:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afb_network', '0010_alter_timeentry_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeentry',
            name='employee',
            field=models.ForeignKey(default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL), on_delete=django.db.models.deletion.CASCADE, to='afb_network.employeeprofile'),
        ),
    ]
