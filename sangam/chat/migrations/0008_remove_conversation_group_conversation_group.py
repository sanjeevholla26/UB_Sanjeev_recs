# Generated by Django 4.1.2 on 2023-05-21 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_remove_conversation_group_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation',
            name='group',
        ),
        migrations.AddField(
            model_name='conversation',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conversations', to='chat.discussion_room'),
        ),
    ]
