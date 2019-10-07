from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User, auth

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"Your account has been created! You are now able to login")
			return redirect('login')
	else:
		form = RegisterForm()
	return render (request, 'accounts/register.html', {'form':form})
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, f"Invalid credentials")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')