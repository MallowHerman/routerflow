from core.utils import BaseModel
from django.db import models

class TelegramBot(BaseModel):
    api_token = models.CharField(max_length=255, unique=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Telegram Bot'
        verbose_name_plural = 'Telegram Bots'

    def __str__(self):
        return self.api_token
