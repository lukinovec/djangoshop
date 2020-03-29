from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Item(models.Model):
	seller = models.ForeignKey(User, on_delete=models.CASCADE)
	itemname = models.CharField(max_length=100)
	price = models.IntegerField()
	about = models.TextField(default="sample text")
	image = models.CharField(default="https://ih1.redbubble.net/image.770583657.2123/flat,750x1000,075,f.u1.jpg", max_length=300)
	date_posted = models.DateField(default=timezone.now)
	date_edited = models.DateField(auto_now=True)
	for_sale = models.BooleanField(default=False)

	def __str__(self):
		return self.itemname

	def get_absolute_url(self):
		return reverse('item-detail', kwargs={'pk': self.pk})


class ItemOwned(Item):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)