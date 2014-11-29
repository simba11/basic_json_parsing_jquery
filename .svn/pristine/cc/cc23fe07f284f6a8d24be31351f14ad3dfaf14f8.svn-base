from django.db import models

class Contact(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	def __unicode__(self):
		return self.first_name
	email = models.EmailField(max_length=75)
	phone = models.CharField(max_length=25)
	notes = models.TextField(default=None)

