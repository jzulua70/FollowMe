from django.db import models

# Create your models here.
from django.contrib.gis.db import models


class Waypoint(models.Model):

    name = models.CharField(max_length=32)
    geometry = models.PointField(srid=4326)
    

    
    def __unicode__(self):
        return '%s %s %s' % (self.name, self.geometry.x, self.geometry.y)