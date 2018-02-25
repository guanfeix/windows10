from django.contrib import admin
from .models import *


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ["pk", "uname", "uphone", "uemail"]


admin.site.register(UserInfo, UserInfoAdmin)