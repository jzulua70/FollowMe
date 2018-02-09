from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.gis.geos import GEOSException, GEOSGeometry
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


def getData(request):
	latitud=request.POST['lat']
	longitud=request.POST['lng']
	hora = request.POST['Hora']
	fecha = request.POST['Fecha']
	current_user = request.user
	id_user = str(current_user.id)
	user_name = str(current_user.username)
	geo=GEOSGeometry('POINT('+longitud+' '+latitud+')')
	Waypoint.objects.create(name=user_name,geometry=geo, user_id=id_user,date=fecha[:10], hour=hora)

	print(request.POST['Hora'])
	return render(request,'getPosition.html')


def index2(request):
	return redirect("/FollowMeApp/index")

# Create your views here.
