from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from core.user.forms import UserAdminChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string

User = get_user_model()

def home_view(request):
    return redirect('dashboard')

@login_required
def dashboard_view(request):
    user = request.user  # Obtém o usuário atualmente autenticado
    user_form = UserAdminChangeForm(instance=user)  # Popula o formulário com os dados do usuário atual

    context = {
        'user_form': user_form
    }
    return render(request, 'core/pages/dashboard.html', context)

@login_required
def update_account_view(request):
    if request.method == 'POST':
        user_form = UserAdminChangeForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            context = {
                'status': 'success',
                'heading': 'Changed', 
                'description': 'Your account information has been updated successfully.'
            }
        else:
            context = {
                'status': 'error',
                'heading': 'Error', 
                'description': 'There was an error updating your account information. Please try again.'
            }
        
        html_content = render_to_string('partials/alert_message.html', context)

        return JsonResponse({
            'username': request.user.username,
            'email': request.user.email,
            'avatar_or_first_letter': request.user.username[0],
            'html': html_content
        })
        
