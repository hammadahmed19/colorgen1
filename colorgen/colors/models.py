from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ColorHash(models.Model):
    user =models.ForeignKey(User , on_delete= models.CASCADE)
    color_hashes = models.JSONField()

    def __str__(self):
        return f"{self.user.username}'s color hash"

