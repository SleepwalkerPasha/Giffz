# Generated by Django 4.0.4 on 2022-05-11 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200601_1522'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RemoveField(
            model_name='like',
            name='created',
        ),
        migrations.RemoveField(
            model_name='like',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]