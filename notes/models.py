from django.db import models

class Snote(models.Model):
    title = models.CharField(max_length=240)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
