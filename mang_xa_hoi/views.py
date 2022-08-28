from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
# from django.http import HttpResponse
from .models import Profile
# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        
        if password == confirmpassword:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username = username, email = email, password = password)
                user.save()
                
            #log user in and redirect to setting page
            
            #create a Profile object for the new user
            
            user_model = User.objects.get(username = username)
            new_profile = Profile.objects.create(user = user_model, id = user_model.id)
            new_profile.save()
        else:
            messages.info(request,'Password not Matching')
            return redirect('signup')
    else:
        return render(request,'signup.html')