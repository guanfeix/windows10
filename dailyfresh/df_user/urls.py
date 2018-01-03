
from django.urls import path,include
from . import views
urlpatterns = [
    path("register/",views.register,name="register"),
    path("login/",views.register,name="register"),
    path("user_center_info/",views.register,name="user_center_info"),
    path("user_center_order/",views.register,name="user_center_order"),
    path("login/",views.register,name="register"),
]
app_name = "df_user"