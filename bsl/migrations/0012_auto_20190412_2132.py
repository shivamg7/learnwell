# Generated by Django 2.2 on 2019-04-12 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bsl', '0011_auto_20190412_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='level',
        ),
        migrations.AddField(
            model_name='user',
            name='lower_bound',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='question_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='upper_bound',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='attempt',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsl.Question'),
        ),
    ]