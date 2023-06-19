from django.conf.urls import url

from register import views

urlpatterns = [

    # url(r'^$', views.index, name='index'),
    url(r'^$', views.user, name='user'),

]
