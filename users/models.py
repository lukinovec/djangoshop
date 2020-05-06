from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.CharField(
        default="https://www.kindpng.com/picc/m/24-248253_user-profile-default-image-png-clipart-png-download.png",
        max_length=300,
    )
    description = models.TextField(
        default="You can change the description on your profile page", max_length=200,
    )
    currency = models.IntegerField(default=1000)

    def __str__(self):
        return f"{self.user.username}'s Profile"
