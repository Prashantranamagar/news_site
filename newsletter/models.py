from django.db import models

class Newsletter(models.Model):
	txt = models.CharField(max_length=50)
	status = models.IntegerField()

	def __str__(self):
		self.txt