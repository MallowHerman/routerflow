from typing import Any
from django import forms
from django.contrib.auth import get_user_model
from django.conf import settings
from core.models import UserProfile

User = get_user_model()

class UserAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
    

    def __init__(self, *args, **kwargs):
        super(UserAccountForm, self).__init__(*args, **kwargs)

        # Personalize os rótulos dos campos, se necessário
        self.fields['username'].label = 'Username'
        
