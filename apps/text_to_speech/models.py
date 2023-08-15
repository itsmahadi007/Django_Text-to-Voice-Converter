from django.db import models


# Create your models here.


class TextToSpeechModel(models.Model):
    text = models.TextField()
    audio = models.FileField(upload_to='audio/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
