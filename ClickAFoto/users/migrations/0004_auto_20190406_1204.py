# Generated by Django 2.2 on 2019-04-06 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190406_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(default='password123', max_length=500),
        ),
    ]