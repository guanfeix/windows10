from django.contrib import admin
from .models import *
# Register your models here.

class ClassifyInfoAdmin(admin.ModelAdmin):
    list_display = ["pk", "title"]
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id',"title","price", "sales", "popularity","stocks","classify"]
# 1.要使用modeladmin个性化管理页面需注册Admin才能显示
admin.site.register(ClassifyInfo,ClassifyInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)