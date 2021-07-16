from django.db import models

# Create your models here.

class Trending(models.Model):

	trending= models.TextField(default='')

	def __str__(self):
		return self.name + "|" + str(self.pk)

