# Generated by Django 4.2.7 on 2023-11-04 16:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gestion_adherents", "0008_alter_equipes_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipes",
            name="points",
            field=models.IntegerField(null=True),
        ),
    ]
