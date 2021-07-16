from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Subcategory(models.Model):
	name = models.CharField(default='-',max_length=50)
	catname = models.CharField(default='-',max_length=50)
	catid= models.IntegerField(default='0')



	def __str__(self):
		return self.name