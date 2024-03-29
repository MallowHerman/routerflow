from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from users.forms import UserAccountForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.utils.translation import gettext as _
from django.utils import translation
from time import sleep

User = get_user_model()

def home_view(request):
    return redirect('dashboard')

@login_required
def dashboard_view(request):
    user_account_form = UserAccountForm(instance=request.user)  # Popula o formulário com os dados do usuário atual

    context = {
        'user_account_form': user_account_form
    }
    return render(request, 'core/pages/dashboard.html', context)

@login_required
def update_account_view(request):
    if request.method == 'POST':
        user = request.user
        user_profile = user.profile
        user_account_form = UserAccountForm(request.POST, instance=user)
        if user_account_form.is_valid():
            user_account_form.save()
            user_profile.language = request.POST.get('language')
            user_profile.save()
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
        
        html_content = render_to_string('partials/alert_message.html', context)

        return JsonResponse({
            'username': request.user.username,
            'avatar_or_first_letter': request.user.username[0],
            'html': html_content
        })
        
