from __future__ import unicode_literals
from django.db import models

# Create your models here.

class News(models.Model):
	name = models.CharField(max_length=500)
	shorttxt = models.TextField()
	bodytxt = models.TextField()
	date = models.CharField(max_length=50, default='-')
	time = models.CharField(max_length=50, default='-')
	picname = models.TextField(default='-')
	picurl = models.TextField(default='-')
	writer = models.CharField(max_length=50)
	catname = models.CharField(max_length=50,default='-')
	catid = models.IntegerField(default=0)
	ocatid = models.IntegerField(default=0)
	show = models.IntegerField(default=0)
	act = models.IntegerField(default=0)

	


	def __str__(self):
		return self.name