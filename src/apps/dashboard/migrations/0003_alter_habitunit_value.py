# Generated by Django 4.2.7 on 2023-12-28 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_habitcategory_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitunit',
            name='value',
            field=models.PositiveIntegerField(),
        ),
    ]
