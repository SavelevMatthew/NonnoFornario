# Generated by Django 3.1.5 on 2021-01-13 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image',
            field=models.ImageField(default=1, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]