# Generated by Django 4.0.1 on 2022-01-12 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_alumno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nombre',
            field=models.CharField(max_length=40, verbose_name='nombre'),
        ),
    ]