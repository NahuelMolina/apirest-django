from django.db import models

class mymodel(models.Model):
	name = models.CharField(max_length = 10)
	last_name = models.CharField(max_length=10)
       
class Customer(models.Model):
        name = models.CharField(max_length = 10)
        nation = models.CharField(max_length = 10)
        total_trans = models.IntegerField()
        partial_doubt = models.FloatField()
        average_revenue = models.FloatField()
