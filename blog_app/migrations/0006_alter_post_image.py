# Generated by Django 5.0.4 on 2024-08-23 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_remove_post_auth_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
