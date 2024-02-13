from core.utils import BaseModel
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class TelegramBot(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="telegram", null=True)
    name = models.CharField(max_length=50, null=True)
    api_token = models.CharField(max_length=255, unique=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Telegram Bot'
        verbose_name_plural = 'Telegram Bots'

    def __str__(self):
        return self.api_token
