from django.views.generic import ListView, DetailView
from pictures.models import Pictures
from django.views.generic.edit import CreateView


# Create your views here.

class PicturesListView(ListView):
    
    model = Pictures
    context_object_name = 'picturesAll'
    template_name = 'pictures/picturesIndex.html'
    
    def get_queryset(self):
        return Pictures.objects.all()
    

class PicturesCreateView(CreateView):
    
    model = Pictures
    fields = ['PictureID', 'Name', 'Description', 'PhotographerID', 'Location', 'Keywords', 'Views', 'Visibility', 'PhotoFile']
    #fiels = "__all__" 
    

class PicturesDetailView(DetailView):
    
    model = Pictures
    template_name = "pictures/pictureDetails.html"