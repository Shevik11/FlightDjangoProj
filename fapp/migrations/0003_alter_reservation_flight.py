# Generated by Django 4.2.3 on 2025-01-11 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("fapp", "0002_alter_flight_dateofdeparture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="flight",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="fapp.flight"
            ),
        ),
    ]
