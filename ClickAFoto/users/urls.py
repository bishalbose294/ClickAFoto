from django.conf.urls import url
from . import views

app_name = 'users'

urlpatterns = [
        
        url(r'^$', views.PhotographersListView.as_view(), name='userIndex'),
                
        url(r"^(?P<pk>[0-9]+)/$", views.PhotographerDetailsView.as_view(), name='users-detail'),
]