# Generated by Django 4.2.7 on 2024-10-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_alter_propertybook_children_alter_propertybook_guest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertybook',
            name='guest',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)]),
        ),
    ]