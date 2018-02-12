from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,

	)
from django import forms

User = get_user_model()
class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		
		# user_qs = User.objects.filter(username=username)
		# if user_qs.count() == 1:
		# 	user =user_qs.first()
		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("this user doesn't exist")

			if not user.check_password(password):
				raise forms.ValidationError("Incorrect password")

			if not user.is_active:
				raise forms.ValidationError("This user is not longer active")

		return super(UserLoginForm,self).clean(*args,**kwargs)


class UserRegisterForm(forms.ModelForm):
	email = forms.EmailField(label= "Email")
	email2 = forms.CharField(label= "Confirm email")
	password= forms.CharField(label= "Password", widget= forms.PasswordInput)
	password2= forms.CharField(label= "Confirm password", widget= forms.PasswordInput)
	class Meta:
		
		model = User
		fields = [
			'username',
			'password',
			'password2'


		]
	def clean_email(self):
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email')
		if email != email2:
			raise forms.ValidationError("Emails must match")
		return email		

		
			
