# Generated by Django 2.0.1 on 2018-01-13 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0017_auto_20180113_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='league',
            name='event',
        ),
        migrations.RemoveField(
            model_name='league',
            name='player1',
        ),
        migrations.RemoveField(
            model_name='league',
            name='player2',
        ),
        migrations.RemoveField(
            model_name='league',
            name='player3',
        ),
        migrations.RemoveField(
            model_name='league',
            name='player4',
        ),
        migrations.AddField(
            model_name='players',
            name='eliminated',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='League',
        ),
    ]