from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, UserLoginForm


class RegisterView(View):
    template_name = 'accounts/register.html'
    form_class = UserRegisterForm
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request, "You don't have access to this page. ", 'danger')
            return redirect('blog:index')
        
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            User.objects.create_user(
                username=cd['username'],
                email=cd['email'],
                first_name=cd['first_name'],
                last_name=cd['last_name'],
                password=cd['password']
            )
            
            messages.success(request, "User created successfully.")
            return redirect('accounts:login')
        
        return render(request, self.template_name, {'form':form})
            
            
    
    
class LoginView(View):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request, "You don't have access to this page. ", 'danger')
            return redirect('blog:index')
        
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password'],
            )
            
            if user:
                login(request, user)
                messages.success(request, "User logged in successfully.")
                return redirect('blog:index')
            else:
                messages.error(request, "Username or password is wrong. ", 'danger')
            
            return render(request, self.template_name, {'form':form})
        
        return render(request, self.template_name, {'form':form})
        

@login_required(login_url='accounts:login')
def user_logout(request):
    logout(request)
    messages.success(request, "User logged out successfully.")
    return redirect('blog:index')
    