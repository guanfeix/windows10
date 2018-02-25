from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path("order/",views.order,name="order"),
    # url(r"^buy_now_(\d+)/$",views.order,name="order"),
    # 这种低级事物，非常非常恶劣的影响脑子不清晰就不要做架构的事情。
    path("order_handle/",views.order_handle,name="order_handle"),
]
app_name = "df_order"