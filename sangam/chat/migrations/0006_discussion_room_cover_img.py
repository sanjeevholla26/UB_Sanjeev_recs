# Generated by Django 4.1.2 on 2023-05-20 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_discussion_room_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion_room',
            name='cover_img',
            field=models.ImageField(blank=True, default='../media/users/user_avtar.webp', null=True, upload_to='discussion_room/'),
        ),
    ]
