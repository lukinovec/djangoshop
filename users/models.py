from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.CharField(default='https://lh3.googleusercontent.com/yVQO8bmGhYjQHYATrXQeaswpZawKBWuiSx1vd4skj2TLMT-JGj8WfPiYFSiULKt0Pg420-zMy_BK7EXV4OTk=s400', max_length=300)
	description = models.TextField(default='tento člověk nám o sobě absolutně nic neřekl, nevěřte mu', max_length=200)
	currency = models.IntegerField(default=1000)

	def __str__(self):
		return f'{self.user.username} Profile'

