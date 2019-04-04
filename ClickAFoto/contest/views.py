from django.views.generic import ListView
from contest.models import Contests

# Create your views here.
class ContestsListView(ListView):
    
    model = Contests
    context_object_name = 'contestsAll'
    template_name = 'contest/contestIndex.html'
    
    def get_queryset(self):
        return Contests.objects.all()