# Generated by Django 2.0.2 on 2018-02-04 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pic/'),
        ),
    ]
