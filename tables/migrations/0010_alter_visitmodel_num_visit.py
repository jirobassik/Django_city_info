# Generated by Django 4.1.1 on 2022-09-29 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0009_alter_objectmodel_address_alter_objectmodel_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitmodel',
            name='num_visit',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество посетивших'),
        ),
    ]