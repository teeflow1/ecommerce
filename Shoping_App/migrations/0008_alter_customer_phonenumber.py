# Generated by Django 4.1 on 2023-03-21 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shoping_App', '0007_remove_customer_phonenumber_customer_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phonenumber',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
