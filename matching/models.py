from django.db import models

class DirectMessage(models.Model):
  sender = models.CharField(max_length=30)
  receiver = models.CharField(max_length=30)
  message = models.CharField(max_length=1000)
  at = models.DateTimeField(auto_now_add=True)
