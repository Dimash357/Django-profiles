# Generated by Django 4.1.3 on 2022-11-24 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0006_alter_todo_bio_alter_todo_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='bio',
            field=models.TextField(blank=True, default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='name',
            field=models.CharField(blank=True, db_index=True, default='', max_length=150, unique=True, verbose_name='Заголовок'),
        ),
    ]
