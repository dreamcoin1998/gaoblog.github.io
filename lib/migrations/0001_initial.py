# Generated by Django 2.0.6 on 2019-02-03 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('author', models.CharField(max_length=10, verbose_name='作者')),
                ('pub_time', models.DateTimeField(auto_now=True, verbose_name='发布时间')),
                ('read_number', models.IntegerField(default=0, editable=False, verbose_name='阅读数')),
                ('text', models.TextField(verbose_name='正文')),
            ],
        ),
        migrations.CreateModel(
            name='Cpomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='评论')),
                ('pub_time', models.DateTimeField(auto_now=True)),
                ('author', models.CharField(max_length=50)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lib.Article')),
            ],
        ),
    ]
