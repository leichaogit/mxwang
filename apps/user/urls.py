from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^login/$', views.UserLoginApi.as_view(), name='login'),
]