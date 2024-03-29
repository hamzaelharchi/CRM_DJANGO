from audioop import reverse
from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views  
from .forms import CustomUserCreationForm, ProfileModelForm, LoginForm
from .models import UserProfile, User

# Create your views here.


class SignUpView(generic.CreateView):
    template_name='registration/signup.html'

    form_class=CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')



class LoginView(auth_views.LoginView):
    form_class=LoginForm
    template_name = 'registration/login.html'
        

    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse('admin:index')
        if self.request.user.type==User.Types.MANAGER:
            return reverse('dashboard:dash')
        elif self.request.user.type==User.Types.CUSTOMER:
            return reverse('shop:product-list')

# Profile views 


class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    template_name ='account/profile.html' 
    context_object_name='userprofile'

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    

class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "account/profile-update.html"
    form_class = ProfileModelForm

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("shop:product-list")

