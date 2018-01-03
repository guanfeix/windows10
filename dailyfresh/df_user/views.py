from django.shortcuts import render

# Create your views here.


def register(re):
    return render(re,"df_user/register.html",context={})


def login(re):
    return render(re,"df_user/login.html",context={})


def user_center_info(re):
    return render(re,"df_user/user_center_info.html",context={})
def user_center_order(re):
    return render(re,"df_user/user_center_order.html",context={})
def user_center_site(re):
    return render(re,"df_user/user_center_site.html",context={})