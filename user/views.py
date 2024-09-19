from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
             # Save the form to create the user
            username = form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')  # Redirect to a success page
    else:
        form = UserRegisterForm()  # Create a new empty form for GET requests

    return render(request, 'user/register.html', {'form': form}) 
