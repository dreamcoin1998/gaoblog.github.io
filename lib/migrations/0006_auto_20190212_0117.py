# Generated by Django 2.0.6 on 2019-02-11 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0005_auto_20190212_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type_all',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='blog_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lib.Type_all'),
        ),
    ]
