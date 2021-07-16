from django.db import models

# Create your models here.
class Contactform(models.Model):
	name = models.CharField(default='-',max_length=100)
	email= models.TextField(default='-')
	msg= models.TextField(default='-')

	


	def __str__(self):
		return self.name + "|" + str(self.pk)