from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from geoApp.models import Waypoint

class device(models.Model) :
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	name_device=models.CharField(max_length=200)




