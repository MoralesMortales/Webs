# Generated by Django 5.0 on 2024-01-31 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default=''),
        ),
    ]
