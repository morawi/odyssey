# Generated by Django 4.0.4 on 2022-05-18 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_1', '0006_alter_attribute_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attributechoice',
            options={'ordering': ['category', 'value'], 'verbose_name': 'Attribute Choice', 'verbose_name_plural': 'Attribute Choices'},
        ),
    ]
