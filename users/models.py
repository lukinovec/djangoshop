from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.CharField(
        default="https://www.kindpng.com/picc/m/24-248253_user-profile-default-image-png-clipart-png-download.png",
        max_length=300,
    )
    description = models.TextField(
        default="Popisek profilu můžete změnit ", max_length=200
    )
    currency = models.IntegerField(default=1000)

    def __str__(self):
        return f"{self.user.username} Profile"
