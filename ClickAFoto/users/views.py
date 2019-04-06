from users.models import Photographers
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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
    fields = ["UserName", "EmailID", "FirstName", "MiddleName", "LastName", "DOB", "Gender",
              "MobileNo", "Nationality", "AddressLine1", "AddressLine2", "AddressLine3", "Pincode", "Bio"]
    
    
class PhotographersUpdateView(UpdateView):
    
    model = Photographers
    fields = ["EmailID", "FirstName", "MiddleName", "LastName", "DOB", "Gender",
              "MobileNo", "Nationality", "AddressLine1", "AddressLine2", "AddressLine3", "Pincode", "Bio"]
    
class PhotograhersDeleteView(DeleteView):
    
    model = Photographers
    success_url = reverse_lazy('users:userIndex')
    
