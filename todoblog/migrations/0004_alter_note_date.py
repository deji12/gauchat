# Generated by Django 4.0.4 on 2022-05-19 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoblog', '0003_alter_task_date_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]
