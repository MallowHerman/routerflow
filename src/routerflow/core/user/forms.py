from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as admin_forms


User = get_user_model()

class UserAdminChangeForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username', 'email']