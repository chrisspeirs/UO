# Generated by Django 2.0 on 2017-12-16 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_auto_20171216_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='olympics',
            name='name',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
    ]
