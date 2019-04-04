from users.models import Photographers
from django.views.generic import ListView

# Create your views here.
class PhotographersListView(ListView):
    
    model = Photographers
    context_object_name = 'photographersAll'
    template_name = 'user/userIndex.html'
    
    def get_queryset(self):
        return Photographers.objects.all()