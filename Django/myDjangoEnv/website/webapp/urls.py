from django.conf.urls import url
from webapp import views


urlpatterns = [
    url(r'^$', views.users, name='users'),
]
