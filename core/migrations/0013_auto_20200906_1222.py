# Generated by Django 3.1.1 on 2020-09-06 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_movie_director'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='director',
            unique_together={('name', 'surname')},
        ),
    ]
