# Generated by Django 4.1.7 on 2023-05-22 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profesor", "0007_profesor_pepe"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profesor", name="pepe", field=models.IntegerField(default=20),
        ),
    ]
