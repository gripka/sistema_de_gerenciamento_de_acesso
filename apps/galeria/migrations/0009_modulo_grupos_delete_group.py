# Generated by Django 5.0.6 on 2024-06-10 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('galeria', '0008_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulo',
            name='grupos',
            field=models.ManyToManyField(to='auth.group'),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]
