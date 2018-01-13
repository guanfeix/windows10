from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path("register/",views.register,name="register"),
    path("register_handle/",views.register_handle,name="register_handle"),
    path("login/",views.login,name="login"),
    path("login_handle/",views.login_handle,name="login_handle"),
    path("info/",views.user_info,name="user_info"),
    path("order/",views.user_order,name="user_order"),
    path("site/",views.user_site,name="user_site"),
    path("logout/", views.logout, name="logout")
]
app_name = "df_user"