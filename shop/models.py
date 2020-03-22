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
	image = models.ImageField(upload_to='item_pics', default='default.png')
	date_posted = models.DateField(default=timezone.now)
	date_edited = models.DateField(auto_now=True)

	def __str__(self):
		return self.itemname

	def get_absolute_url(self):
		return reverse('item-detail', kwargs={'pk': self.pk})

	def save(self):
		super().save()
		img = Image.open(self.image.path)
		if (img.height > 200 or img.width > 200) or (img.height < 200 or img.width < 200):
			output_size = (200, 200)
			img.thumbnail(output_size)
			img.save(self.image.path)