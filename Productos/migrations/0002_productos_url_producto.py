# Generated by Django 5.0.6 on 2024-05-08 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='url_producto',
            field=models.TextField(null=True),
        ),
    ]
