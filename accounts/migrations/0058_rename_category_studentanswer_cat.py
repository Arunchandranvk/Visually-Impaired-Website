# Generated by Django 4.2.7 on 2023-12-26 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0057_studentanswer_audio_studentanswer_suggestion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentanswer',
            old_name='category',
            new_name='cat',
        ),
    ]
