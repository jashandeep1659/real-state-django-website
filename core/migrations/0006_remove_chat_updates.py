# Generated by Django 4.1.1 on 2022-11-04 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_chat_alter_building_images_building_message"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="chat",
            name="updates",
        ),
    ]
