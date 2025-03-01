from django.shortcuts import render
from user_profile.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        address_user = request.POST.get('address')
        password = request.POST.get('password')

        User.objects.create(username = username, email = email, address = address_user,password = password)
        return redirect('user_profile/login/')
    else:
        return render(request,'register.html')

def login_page(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        try:
            user = User.objects.get(email = user_email, password = user_password)
            print("Login Succesful")
            request.session['username'] = user.username
            request.session['useremail'] = user.email
            return redirect('blog/blog_page/')

        except:
            return HttpResponse("LOGIN FAILED")



        