# Generated by Django 3.1.1 on 2020-09-15 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20200915_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoscursos',
            name='inicio',
            field=models.DateTimeField(verbose_name='Started from'),
        ),
    ]
