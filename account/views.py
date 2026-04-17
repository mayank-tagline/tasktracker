from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views 


# class HomeView(LoginRequiredMixin , View ):
#     login_url = '/login/'
#     redirect_field_name = ''
#     def get(self, request):
#         return render(request, "home.html")
    
# class LoginView(django_auth_views.LoginView):
#     template_name = 'login.html'
#     extra_context = None
#     redirect_authenticated_user = True
    
class LoginView(views.LoginView):
    # redirect_authenticated_user = True
    login_url = '/login/'
    redirect_field_name = ''
    def get(self, request):
        return render(request, "login.html")
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username= username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('login')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('login')
        else:
            login(request, user)
            return redirect('home')
        

class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('register')
        
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        user.set_password(password)
        user.save()
        messages.info(request, "Account created Successfully!")
        return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')