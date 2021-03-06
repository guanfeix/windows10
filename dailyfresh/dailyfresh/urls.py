"""dailyfresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/",include("df_user.urls",namespace="df_user")),
    path("goods/",include("df_goods.urls",namespace="df_goods")),
    path('tinymce/', include('tinymce.urls',),),
    path("",include("df_cart.urls",namespace="df_cart")),
    path("",include("df_order.urls",namespace="df_order")),
    # path("search/", include("haystack.urls")),
]
