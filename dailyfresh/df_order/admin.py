from django.contrib import admin
from .models import *

class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ["id","user","IsPay","total","address"]


class OrderDetailInfoAdmin(admin.ModelAdmin):
    list_display = ["pk","order","goods","price","count"]

# Register your models here.

# 顺序也有要求
admin.site.register(OrderInfo,OrderInfoAdmin,)
admin.site.register(OrderDetailInfo,OrderDetailInfoAdmin,)