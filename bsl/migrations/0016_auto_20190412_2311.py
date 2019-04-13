# Generated by Django 2.2 on 2019-04-12 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bsl', '0015_auto_20190412_2310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='cSUm',
            new_name='cSum',
        ),
        migrations.AlterField(
            model_name='attempt',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsl.Question'),
        ),
    ]
