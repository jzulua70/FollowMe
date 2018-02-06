from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import Waypoint

def map(request):
	waypoints = Waypoint.objects.order_by('name')	
	context = {'waypoints':waypoints ,'content': render_to_string('waypoints.html', {'waypoints': waypoints}),}
	return render(request, 'index2.html', context)
	


# Create your views here.
