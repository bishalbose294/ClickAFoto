# Generated by Django 2.2 on 2019-04-05 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190405_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographers',
            name='Pincode',
            field=models.CharField(max_length=6),
        ),
    ]
