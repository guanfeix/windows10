from django.contrib import admin
from .models import *
# Register your models here.
class CartInfoAdmin(admin.ModelAdmin):
    list_display = ["pk","goods","count","master"]
admin.site.register(CartInfo,CartInfoAdmin)