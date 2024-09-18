from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
             # Save the form to create the user
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')  # Redirect to a success page
    else:
        form = UserCreationForm()  # Create a new empty form for GET requests

    return render(request, 'user/register.html', {'form': form})
