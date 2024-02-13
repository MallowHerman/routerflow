
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.forms import UserAccountForm
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext as _
from telegram.models import TelegramBot
from telegram.forms import TelegramBotForm


@login_required
def settings_modal_account(request):
    user_account_form = UserAccountForm(instance=request.user)  # Popula o formulário com os dados do usuário atual

    context = {
        'user_account_form': user_account_form
    }
    return render(request, 'partials/settings_account.html', context)


@login_required
def settings_modal_password(request):
    password_change_form = PasswordChangeForm(request.user)

    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            password_change_form.save()
            # Optionally, you can add a success message here
            # Add appropriate logic for success message
            context = {
                'status': 'success',
                'heading': 'Changed', 
                'description': _('Your account information has been updated successfully.')
            }
        else:
            context = {
                'status': 'error',
                'heading': 'Error', 
                'description': _('There was an error updating your account information. Please try again.')
            }

        return render(request, 'partials/alert_message.html', context)

    context = {
        'password_change_form': password_change_form
    }

    return render(request, 'partials/settings_password.html', context)

 
@login_required
def settings_modal_telegram(request):
    telegram_bot = TelegramBot.objects.filter(user=request.user).first()

    if request.method == 'POST':
        form = TelegramBotForm(request.POST, instance=telegram_bot)
        if form.is_valid():
            telegram_bot = form.save(commit=False)
            telegram_bot.user = request.user
            telegram_bot.save()
            context = {
                'status': 'success',
                'heading': _('Changed'), 
                'description': _('Your account information has been updated successfully.')
            }
        else:
            context = {
                'status': 'error',
                'heading': _('Error'), 
                'description': _('There was an error updating your account information. Please try again.')
            }

        if request.htmx:
            return render(request, 'partials/alert_message.html', context)
    else:
        form = TelegramBotForm(instance=telegram_bot)

    context = {
        'form': form,
        'telegram_bot': telegram_bot
    }
    
    return render(request, 'partials/settings_telegram.html', context)
