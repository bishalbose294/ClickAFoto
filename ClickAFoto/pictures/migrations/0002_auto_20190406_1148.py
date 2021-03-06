# Generated by Django 2.2 on 2019-04-06 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('pictures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratings',
            name='PhotographerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Photographers'),
        ),
        migrations.AddField(
            model_name='ratings',
            name='PictureID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pictures.Pictures'),
        ),
        migrations.AddField(
            model_name='pictures',
            name='PhotographerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Photographers'),
        ),
        migrations.AddField(
            model_name='likes',
            name='PhotographerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Photographers'),
        ),
        migrations.AddField(
            model_name='likes',
            name='PictureID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pictures.Pictures'),
        ),
        migrations.AddField(
            model_name='comments',
            name='PhotographerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Photographers'),
        ),
        migrations.AddField(
            model_name='comments',
            name='PictureID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pictures.Pictures'),
        ),
    ]
