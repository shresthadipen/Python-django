from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created successfully!")
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})

class CustomLogout(LogoutView):
    http_method_names=['get', 'post', 'options']
