# Generated by Django 4.0.4 on 2022-05-18 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_1', '0005_alter_attribute_options_alter_file_occurrence_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attribute',
            options={'ordering': ['value__category', 'value'], 'verbose_name': 'Attribute', 'verbose_name_plural': 'Attributes'},
        ),
    ]
