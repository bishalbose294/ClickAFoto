from django.conf.urls import url
from . import views

app_name = 'users'

urlpatterns = [
                url(r'^$', views.PhotographersListView.as_view(), name='userIndex'),
]