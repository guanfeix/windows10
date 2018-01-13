from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path("index/", views.index, name="index"),
    # path("",views)
    url(r"^list_(\d+)_(\d+)/$", views.list, name="list"),
    path("detail/",views.detail, name="detail")

]
app_name = "df_goods"