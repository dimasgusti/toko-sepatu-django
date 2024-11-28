# account/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # Your custom User model

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    telephone = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, initial='user', disabled=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'telephone', 'address', 'role', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user