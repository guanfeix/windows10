from django.conf.urls import url
from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path("index/", views.index, name="index"),
    url(r"^list1_(\d+)_(\d+)/$", views.list1, name="list"),
    path("detail/",views.detail, name="detail"),
    path("search/", FacetedSearchView(),name='search_view'),

]
app_name = "df_goods"