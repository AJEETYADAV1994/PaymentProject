# Generated by Django 4.1.2 on 2022-10-11 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Paymentapp", "0003_coffee_email_coffee_mobile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coffee",
            name="email",
            field=models.EmailField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name="coffee",
            name="mobile",
            field=models.CharField(blank=True, max_length=12),
        ),
    ]