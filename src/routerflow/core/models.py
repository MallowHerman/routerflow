from django.db import models
from django.contrib.auth import get_user_model
from core.utils import BaseModel
from django.conf import settings


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
    language = models.TextField(
        max_length=10,
        choices=settings.LANGUAGES,
        default=settings.LANGUAGE_CODE,
        help_text="An ISO 639 language code (with optional variant) "
        "selected by the user. Ex: en-GB.",
    )

    def __str__(self) -> str:
        return f"{self.user.username}'s profile"