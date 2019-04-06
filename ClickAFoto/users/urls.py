from django.conf.urls import url
from . import views

app_name = 'users'

urlpatterns = [
        
        url(r'^$', views.PhotographersListView.as_view(), name='userIndex'),
                
        url(r"^(?P<pk>[0-9]+)/$", views.PhotographerDetailsView.as_view(), name='users-detail'),
        
        url(r"add/$", views.PhotographersCreateView.as_view(), name='users-add'),
        
        url(r"(?P<pk>[0-9]+)/update/$", views.PhotographersUpdateView.as_view(), name='users-update'),
        
        url(r"(?P<pk>[0-9]+)/delete/$", views.PhotograhersDeleteView.as_view(), name='users-delete'),
        
        url(r"^register/$",views.UserFormView.as_view(), name="register"),
]