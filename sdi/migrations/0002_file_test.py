# Generated by Django 4.0.4 on 2022-05-30 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='test',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
