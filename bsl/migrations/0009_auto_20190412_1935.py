# Generated by Django 2.2 on 2019-04-12 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bsl', '0008_auto_20190412_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='question',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bsl.Question'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
