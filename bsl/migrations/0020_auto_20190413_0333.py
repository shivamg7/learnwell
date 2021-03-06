# Generated by Django 2.2 on 2019-04-13 03:33

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bsl', '0019_auto_20190413_0148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stats',
            name='confidenceLevel',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='postSkill',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='preSkill',
        ),
        migrations.AddField(
            model_name='stats',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 13, 3, 33, 36, 22901, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='attempt',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsl.Question'),
        ),
    ]
