# Generated by Django 5.0.6 on 2024-05-08 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='descripcion',
        ),
    ]
