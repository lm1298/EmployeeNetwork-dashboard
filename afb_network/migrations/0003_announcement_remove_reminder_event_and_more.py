# Generated by Django 5.0.6 on 2024-07-05 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afb_network', '0002_employeeprofile_department_employeeprofile_end_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='event',
        ),
        migrations.AddField(
            model_name='reminder',
            name='event_title',
            field=models.CharField(default='Reminder', max_length=255),
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]