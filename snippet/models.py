from django.db import models

class mymodel(models.Model):
	name = models.CharField(max_length = 10)
	last_name = models.CharField(max_length=10)

