
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.user.forms import UserAccountForm
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext as _


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


    
