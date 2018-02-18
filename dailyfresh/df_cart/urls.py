from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path("cart/",views.cart,name="cart"),
    url(r"^buy_(\d+)_(\d+)/$", views.buy, name="order"),
    url(r"^add_(\d+)_(\d+)/",views.add,name="add"),
    url(r"^edit(\d+)_(\d+)/$",views.edit,name="edit"),
    url(r"^delete(\d+)/$",views.delete,name="delete"),
]
app_name = "df_cart"