# Generated by Django 2.2 on 2019-04-13 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bsl', '0017_auto_20190412_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='attempt',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsl.Question'),
        ),
        migrations.AlterField(
            model_name='stats',
            name='quizid',
            field=models.IntegerField(default=0),
        ),
    ]
