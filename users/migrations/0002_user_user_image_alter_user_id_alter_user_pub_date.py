# Generated by Django 4.2.2 on 2023-06-21 09:52

import datetime
from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_image',
            field=models.ImageField(default='profile_pic/image.jpg', upload_to=users.models.image_path),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 21, 9, 52, 46, 193272, tzinfo=datetime.timezone.utc)),
        ),
    ]
