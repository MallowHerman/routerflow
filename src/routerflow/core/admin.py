from django.contrib import admin
from core.models import UserProfile
from core.telegram.models import TelegramBot

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(TelegramBot)
class TelegramBotAdmin(admin.ModelAdmin):
    pass
