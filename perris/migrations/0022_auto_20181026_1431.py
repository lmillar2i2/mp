# Generated by Django 2.1.2 on 2018-10-26 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perris', '0021_auto_20181025_2145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perros_rescatados',
            options={'permissions': (('adoptantes', 'Adoptantes'),)},
        ),
    ]
