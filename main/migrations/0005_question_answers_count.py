# Generated by Django 3.0.5 on 2020-04-17 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200415_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answers_count',
            field=models.IntegerField(default=0),
        ),
    ]
