# Generated by Django 2.2 on 2019-04-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsl', '0005_auto_20190412_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('ECO', 'Economics'), ('HIS', 'History'), ('BAK', 'Banking'), ('GOV', 'Government'), ('PSY', 'Psycology')], max_length=3),
        ),
    ]
