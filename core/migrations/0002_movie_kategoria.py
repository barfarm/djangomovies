# Generated by Django 3.1.1 on 2020-09-05 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='kategoria',
            field=models.CharField(default='triller', max_length=50),
            preserve_default=False,
        ),
    ]