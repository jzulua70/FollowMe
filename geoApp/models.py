from django.db import models

# Create your models here.
from django.contrib.gis.db import models
from django.contrib.auth.models import User

class Waypoint(models.Model):

	name = models.CharField(max_length=32)
	hour = models.CharField(max_length=32)
	date = models.CharField(max_length=32)
	geometry = models.PointField(srid=4326)
	user= models.ForeignKey(User, on_delete=models.CASCADE)


	
	
	def __unicode__(self):
		return '%s %s %s' % (self.name, self.geometry.x, self.geometry.y)