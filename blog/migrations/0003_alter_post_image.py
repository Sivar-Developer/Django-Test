# Generated by Django 4.0 on 2022-01-14 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to='images/'),
        ),
    ]
