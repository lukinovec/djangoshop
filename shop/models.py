from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Item(models.Model):
	seller = models.ForeignKey(User, on_delete=models.CASCADE)
	itemname = models.CharField(max_length=100)
	price = models.IntegerField()
	about = models.TextField()
	image = models.TextField(default="")
	date_posted = models.DateField(default=timezone.now)
	date_edited = models.DateField(auto_now=True)

	def __str__(self):
		return self.itemname