# Generated by Django 2.1.7 on 2019-02-20 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0013_auto_20190220_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发布时间'),
        ),
    ]
