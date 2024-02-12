from django.db import models
from django.contrib.auth import get_user_model
from core.utils import BaseModel


User = get_user_model()


class UserProfile(BaseModel):
    class TelegramNotificationFrequencyOptions(models.TextChoices):
        INSTANT = "instant", "instant"
        DAILY = "daily", "daily"
        WEEKLY = "weekly", "weekly"
        NEVER = "never", "never"

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    telegram_notification_frequency = models.TextField(
        max_length=16,
        choices=TelegramNotificationFrequencyOptions.choices,
        default=TelegramNotificationFrequencyOptions.INSTANT,
    )