# Generated by Django 3.1.1 on 2020-09-06 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200906_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='age_limit',
            field=models.IntegerField(choices=[(0, 0), (6, 6), (12, 12), (15, 15), (18, 18)], default='NA', max_length=3),
        ),
    ]
