# Generated by Django 4.0.4 on 2022-05-14 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0006_alter_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='view_profile_pic',
            field=models.BooleanField(default=False),
        ),
    ]