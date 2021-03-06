from django.conf.urls import url
from . import views

app_name = "drug"

urlpatterns = [
    url(r'^report_drug/$', views.report_drug, name="report_drug"),
    url(r'^report_order/$', views.report_order, name="report_order"),
    url(r'^report_resource/$', views.report_resource, name="report_resource"),

    url(r'^drug_detail/$', views.drug_detail, name="drug_detail"),
    url(r'^drug_order/$', views.drug_order, name="drug_order"),

    url(r'^commend/$', views.commend, name="commend"),
    url(r'^reviews/$', views.reviews, name="reviews"),
    url(r'^reviews_percostumer/(?P<id>[0-9]+)/$', views.reviews_percostumer, name="reviews_percostumer"),
    url(r'^review_new/(?P<id>[0-9]+)/$', views.review_details_new, name="review_details_new"),

    url(r'^onosh_new/$', views.onosh_create, name="onosh_create"),
    url(r'^onosh_list/$', views.onosh_list, name="onosh_list"),

    url(r'^history_new/$', views.history_create, name="history_create"),
    url(r'^history_list/$', views.history_list, name="history_list"),

    url(r'^emchilgee_new/$', views.emchilgee_create, name="emchilgee_create"),
    url(r'^emchilgee/(?P<id>[0-9]+)/$', views.emchilgee_details, name="emchilgee_details"),
    url(r'^emchilgee_list/$', views.emchilgee_list, name="emchilgee_list"),
    url(r'^all_emchilgee_list/$', views.all_emchilgee_list, name="all_emchilgee_list"),
    url(r'^costumer_emchilgee_list/$', views.costumer_emchilgee_list, name="costumer_emchilgee_list"),
    url(r'^emchilgee_list_done/$', views.emchilgee_list_done, name="emchilgee_list_done"),

    url(r'^add_recived_date/(?P<id>[0-9]+)/$', views.add_recived_date, name = "add_recived_date"),

    url(r'^morning/(?P<id>[0-9]+)/$', views.morning, name="morning"),
    url(r'^afternoon/(?P<id>[0-9]+)/$', views.afternoon, name="afternoon"),
    url(r'^evening/(?P<id>[0-9]+)/$', views.evening, name="evening"),

    url(r'^make_review_1/(?P<emchilgee_id>[0-9]+)/$', views.make_review_1, name="make_review_1"),
    url(r'^make_review_2/(?P<emchilgee_id>[0-9]+)/$', views.make_review_2, name="make_review_2"),
    url(r'^make_review_3/(?P<emchilgee_id>[0-9]+)/$', views.make_review_3, name="make_review_3"),
    url(r'^make_review_4/(?P<emchilgee_id>[0-9]+)/$', views.make_review_4, name="make_review_4"),
    url(r'^make_review_5/(?P<emchilgee_id>[0-9]+)/$', views.make_review_5, name="make_review_5"),
]
