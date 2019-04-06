from users.models import Photographers, Login
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate,login
from .forms import UserForm

# Create your views here.
class PhotographersListView(ListView):
    
    model = Photographers
    context_object_name = 'photographersAll'
    template_name = 'users/userIndex.html'
    
    def get_queryset(self):
        return Photographers.objects.all()
    
    
class PhotographerDetailsView(DetailView):
    
    model = Photographers
    template_name = 'users/userDetails.html'
    
    
class PhotographersCreateView(CreateView):
    
    model = Photographers
    fields = ["username", "EmailID", "FirstName", "MiddleName", "LastName", "DOB", "Gender",
              "MobileNo", "Nationality", "AddressLine1", "AddressLine2", "AddressLine3", "Pincode", "Bio"]
    
    
class PhotographersUpdateView(UpdateView):
    
    model = Photographers
    fields = ["EmailID", "FirstName", "MiddleName", "LastName", "DOB", "Gender",
              "MobileNo", "Nationality", "AddressLine1", "AddressLine2", "AddressLine3", "Pincode", "Bio"]
    
class PhotograhersDeleteView(DeleteView):
    
    model = Photographers
    success_url = reverse_lazy('users:userIndex')
    
    
class UserFormView(View):
    
    form_class = UserForm
    template_name = 'users/registration_form.html'
    
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})
    
    def post(self,request):
        
        form = self.form_class(request.POST)
        
        if form.is_valid():
            
            user = form.save(commit = False)
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user.set_password(password)
            
            user.save()
            
            user = authenticate(username=username,password=password)
            
            if user is not None:
                
                if user.is_active:
                    
                    login(request,user)
                    return redirect('users:users-add')
                
        return render(request, self.template_name, {'form' : form})
                    
                    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
