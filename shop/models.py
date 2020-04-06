from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Item(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    itemname = models.CharField(max_length=100)
    price = models.IntegerField()
    about = models.TextField(default="sample text", max_length=400)
    image = models.CharField(
        default="https://i.pinimg.com/originals/c4/59/ac/c459ac0f3a776c5b03e2b9595e611288.jpg",
        max_length=300,
    )
    date_posted = models.DateField(default=timezone.now)
    date_edited = models.DateField(auto_now=True)
    for_sale = models.BooleanField(default=True)
    original = models.CharField(max_length=200)

    def __str__(self):
        return self.itemname

    def get_absolute_url(self):
        return reverse("item-detail", kwargs={"pk": self.pk})
