# Generated by Django 4.2.10 on 2024-02-12 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_telegrambot_api_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='language',
            field=models.TextField(choices=[('en', 'English'), ('pt', 'Portuguese')], default='en-us', help_text='An ISO 639 language code (with optional variant) selected by the user. Ex: en-GB.', max_length=10),
        ),
    ]
