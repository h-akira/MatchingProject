from .models import DirectMessage
from django import forms

class DirectMessageForm(forms.ModelForm):
  class Meta:
    model = DirectMessage
    fields = ('message',)  # 要素数1のタプルにするためにカンマをつける
