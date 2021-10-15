

from django.http import response
from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.

def home(request):
    if request.session.has_key('log'):
        return render(request, 'home.html')
    else:
        return render(request, 'login.html') #donot render login page in the home route, instead redirect to login page


    
    

def login(request):
    if request.session.has_key('log'):
        return redirect('home') #donot render home page in the login route, instead redirect to home page
    else:

        if request.method == 'POST':
            
            username = request.POST['username']
            password = request.POST['password']

            print(username, password)

            if username =='admin' and password =='1234':
                request.session['log']= True
                return redirect('home')
            else:
                print("haaaaaaa")
                messages.info(request, 'Incorrect username or password')
                return redirect('login')
        else:
            return redirect('home')
        

    

def logout(request):
    if request.session.has_key('log'):

        request.session.flush()
        return redirect('home')
    else:
        return redirect('home')