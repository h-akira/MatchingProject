from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
  class Meta:
    model = CustomUser
    fields = ("last_name", "first_name", "registration_type","profile")
