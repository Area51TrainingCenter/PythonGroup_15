# Generated by Django 2.1 on 2018-08-18 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_company_software'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Software',
        ),
    ]