from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import Waypoint

def map(request):
	current_user = request.user
	id_user = str(current_user.id)
	waypoints = Waypoint.objects.filter(user_id=id_user).order_by('name')	
	print(waypoints)
	context = {'waypoints':waypoints ,'content': render_to_string('waypoints.html', {'waypoints': waypoints}),}
	return render(request, 'mainPageGeo.html', context)
	

def getPosition(request):
	return render(request,'getPosition.html')
# Create your views here.
