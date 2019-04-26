from django.conf.urls import url
from . import views

app_name = "drug"

urlpatterns = [
    url(r'^drug_detail/$', views.drug_detail, name="drug_detail"),
    url(r'^emchilgee_new/$', views.emchilgee_create, name="emchilgee_create"),
    url(r'^onosh_new/$', views.onosh_create, name="onosh_create"),
    url(r'^onosh_list/$', views.onosh_list, name="onosh_list"),
    url(r'^history_new/$', views.history_create, name="history_create"),
    url(r'^history_list/$', views.history_list, name="history_list"),
    url(r'^emchilgee_list/$', views.emchilgee_list, name="emchilgee_list"),
]
