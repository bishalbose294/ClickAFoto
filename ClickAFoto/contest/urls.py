from django.conf.urls import url
from contest import views

app_name = 'contest'

urlpatterns = [
                url(r'^$', views.ContestsListView.as_view(), name='contestIndex'),
]