from django.shortcuts import render, redirect
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,

	)

from django.http import HttpResponse

from .forms import UserLoginForm
from .forms import UserRegisterForm


def index(request):
    return render(request, 'index.html')

def login_view(request):
	print(request.user.is_authenticated)
	form = UserLoginForm(request.POST or None)
	title= "login"
	context={'form':form, 'title':title }
	if form.is_valid():
		username=  form.cleaned_data.get("username")
		password=  form.cleaned_data.get("password")
		user = authenticate(username=username,password=password)
		login(request,user)
		print(request.user.is_authenticated)
		# redirect
		return redirect("/FollowMeApp/index")


	return render(request, 'login_view.html', context)

def register_view(request):
	title =  "register"
	form = UserRegisterForm(request.POST or None)

	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get("password")
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username,password=user.password)
		login(request,user)
		return redirect("/FollowMeApp/index")

	context = {
		"form":form,
		"title":title
	}
	return render(request, 'register.html',context)

def logout_view(request):
	logout(request)
	return redirect("/FollowMeApp/index")
	return render(request, 'register.html',{})

def register(request):
    return render(request, 'register.html')
  