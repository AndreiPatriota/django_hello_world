# Generated by Django 3.1.1 on 2020-09-15 00:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_todoscursos_inicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoscursos',
            name='inicio',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 15, 0, 43, 33, 192426, tzinfo=utc), verbose_name='Started from'),
            preserve_default=False,
        ),
    ]
