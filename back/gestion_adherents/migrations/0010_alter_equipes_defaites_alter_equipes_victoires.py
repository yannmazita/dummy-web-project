# Generated by Django 4.2.7 on 2023-11-04 16:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gestion_adherents", "0009_alter_equipes_points"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipes",
            name="defaites",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="equipes",
            name="victoires",
            field=models.IntegerField(null=True),
        ),
    ]
