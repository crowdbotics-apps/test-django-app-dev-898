# Generated by Django 2.2.4 on 2019-08-19 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("home", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="customtext",
            name="title",
            field=models.CharField(blank=True, max_length=150),
        )
    ]