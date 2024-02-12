
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.user.forms import UserAccountForm


@login_required
def settings_modal_account(request):
    user_account_form = UserAccountForm(instance=request.user)  # Popula o formulário com os dados do usuário atual

    context = {
        'user_account_form': user_account_form
    }
    return render(request, 'partials/settings_account.html', context)
