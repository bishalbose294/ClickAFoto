# Generated by Django 2.2 on 2019-04-06 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_login_photographerid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='LastLoginTimestamp',
        ),
        migrations.RemoveField(
            model_name='login',
            name='TimeStamp',
        ),
        migrations.AlterField(
            model_name='login',
            name='date_joined',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='login',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='login',
            name='last_login',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
