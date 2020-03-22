from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.png', upload_to='profile_pics')
	description = models.TextField(default='tento člověk nám o sobě absolutně nic neřekl, nevěřte mu', max_length=200)

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)
		image = Image.open(self.image.path)
		if (image.height > 200 or image.width > 200) or (image.height < 200 or image.width < 200):
			output_size = (200, 200)
			image.thumbnail(output_size)
			image.save(self.image.path)
