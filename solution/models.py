from django.db import models
from django.contrib.auth.models import User

class UserXmlFile(models.Model):
	owner = models.OneToOneField(User, on_delete=models.CASCADE)
	url = models.TextField()
	xmlContent = models.TextField()
	
	def __str__(self):
		return self.owner.username + ' - ' + self.url
