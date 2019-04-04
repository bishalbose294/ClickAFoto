from django.conf.urls import url
from . import views

app_name = 'pictures'

urlpatterns = [

url(r"^$", views.PicturesListView.as_view(), name='picturesIndex'),


url(r"add/$", views.PicturesCreateView.as_view(), name='pictures-add'),


url(r"^(?P<pk>[0-9]+)/$", views.PicturesDetailView.as_view(), name='pictures-detail'),

]