# Generated by Django 4.2.3 on 2023-07-31 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_remove_productitem_gender_id_productitem_gender_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="title",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]