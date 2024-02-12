from typing import Any
from django import forms
from django.contrib.auth import get_user_model
from django.conf import settings
from core.models import UserProfile

User = get_user_model()

class UserAccountForm(forms.ModelForm):
    language = forms.ChoiceField(choices=settings.LANGUAGES)
    class Meta:
        model = User
        fields = ['username', 'language']
    

    def __init__(self, *args, **kwargs):
        super(UserAccountForm, self).__init__(*args, **kwargs)

        # Personalize os rótulos dos campos, se necessário
        self.fields['username'].label = 'Username'
        self.fields['language'].label = 'Interface language'

    def save(self, commit: bool = ...) -> Any:
        user = super(UserAccountForm, self).save(commit=False)
        language_selected = self.cleaned_data['language']
        user_profile = user.profile
        user_profile.language = language_selected
        user_profile.save()

        return user
        
