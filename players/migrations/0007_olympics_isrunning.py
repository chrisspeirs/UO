# Generated by Django 2.0 on 2017-12-18 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_auto_20171218_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='olympics',
            name='isRunning',
            field=models.BooleanField(default=False),
        ),
    ]