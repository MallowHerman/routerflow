from django import forms
from telegram.models import TelegramBot

class TelegramBotForm(forms.ModelForm):
    class Meta:
        model = TelegramBot
        fields = ['name', 'api_token']