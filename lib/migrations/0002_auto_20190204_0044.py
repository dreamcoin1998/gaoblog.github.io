# Generated by Django 2.0.6 on 2019-02-03 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='read_number',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='阅读数'),
        ),
    ]
