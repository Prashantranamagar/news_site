from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Manager(models.Model):
	name = models.CharField(default='-',max_length=100)
	utxt= models.TextField(default='-')
	email= models.TextField(default='-')
	ip= models.TextField(default='-')
	country= models.TextField(default='-')




	


	def __str__(self):
		return self.name + "|" + str(self.pk)