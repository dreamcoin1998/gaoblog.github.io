# Generated by Django 2.1.7 on 2019-02-20 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0015_article_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
    ]
