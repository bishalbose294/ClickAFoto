from users.models import Photographers
from django.views.generic import ListView, DetailView

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