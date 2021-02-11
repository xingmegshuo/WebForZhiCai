# Generated by Django 3.1.6 on 2021-02-04 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(help_text='图片', upload_to='media/pic', verbose_name='图片')),
                ('desc', models.TextField(help_text='图片介绍', verbose_name='图片介绍')),
            ],
            options={
                'verbose_name': '展示介绍',
                'verbose_name_plural': '展示介绍',
            },
        ),
    ]
