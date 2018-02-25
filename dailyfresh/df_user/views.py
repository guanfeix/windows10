from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

from .models import *
from df_goods.models import * #0.霸王硬上弓
from df_order.models import *

from hashlib import sha1
from .user_decorator import check_login
# Create your views here.


def register(re):
    return render(re,"df_user/register.html",context={})
def register_handle(request):
    #接收页面信息
    post = request.POST
    uname = post.get("user_name")
    upwd1 = post.get("pwd")
    upwd2 = post.get("cpwd")
    uemail = post.get("email")
    #判断两次密码
    if upwd1 != upwd2:
        return redirect("/user/register/")
    #密码加密
    s1 = sha1()
    s1.update(upwd1.encode("utf-8"))
    upwd = s1.hexdigest()
    #映射
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd
    user.uemail = uemail
    user.save()
    return redirect("/user/login/")#1.重定向是打开一个新的url所以要写匹配的path


def login_handle(request):
    post = request.POST
    uname = post.get("username")#2.这里没有id传的是键值对name，value
    pwd = post.get("pwd")#4.post刷新里面的信息就丢失了需重新输入故别浪费时间在这里
    remember = post.get("remember",0)
    try:
        s2 = sha1()
        s2.update(pwd.encode("utf-8"))
        upwd1 = s2.hexdigest()
        user = UserInfo.objects.get(uname=uname)#3.models class manager -objects django与db交互的接口
        upwd2 = user.upwd        #5.filte得到[],get None 如果是空数组就会出错，用异常捕捉解决4，5的问题,

        if upwd1 == upwd2:
            url = request.COOKIES["url"]
            print("login-url",url)
            red = HttpResponseRedirect(url)
            red.set_cookie("uname", value=uname, max_age=1800)
            # if remember==1:
            #     red.set_cookie("uname",value=uname,max_age=300)
            # else:
            #     red.set_cookie("uname",value="",max_age=-1)

            request.session["user_id"] = user.id # 没记忆6.Httprequest 属性类字典对象
            request.session["user_name"] = user.uname
            request.session.set_expiry(3000)
            # context={"user":user, "page_name": 0}

            return red#7.我的写法至少对我来讲是有用的
            # return HttpResponseRedirect("/user/user_center_info/",context)#7.没卵用增加了cookie，session
        else:
            return redirect("/user/login/")
    except Exception as e:
        print(e)
        return redirect("/user/login/")



def login(re):
    user_name = re.session.get("user_name")
    if user_name:
        url = re.COOKIES["url"]
        return HttpResponseRedirect(url)
    return render(re,"df_user/login.html",context={})


@check_login
def user_info(request):
    user_name = request.session.get("user_name")
    id = request.session.get("user_id")
    user = UserInfo.objects.get(pk=id)
    recent_list_str = request.COOKIES.get("recent_list_str")
    print("recent_list_str",recent_list_str)
    goodslist = []
    if recent_list_str:
        recent_list =recent_list_str.split(",")
        for id in recent_list:
            goods = GoodsInfo.objects.get(pk=int(id))
            goodslist.append(goods)
    context = {"user": user, "page_name": 1,
                   "user_name": user_name,"goodslist":goodslist }
    return render(request,"df_user/user_center_info.html",context)


@check_login
def user_order(request,page_id):
    user_name = request.session.get("user_name")
    user_id = request.session.get("user_id")

    orderinfos = OrderInfo.objects.filter(user=user_id)

    # 分页
    paginator = Paginator(orderinfos,2)
    page = paginator.page(int(page_id))

    user = UserInfo.objects.get(pk=user_id)

    context = {"user": user, "page_name": 2,
               "user_name": user_name,
               "page":page, "paginator":paginator}
    return render(request,"df_user/user_center_order.html",context)


@check_login
def user_site(request):
    # 8.获取数据的几种方式 session，GET,自查（结合了session因为是个变量）都用了。cookie还不会
    user_name = request.session.get("user_name")
    id = request.session.get("user_id")
    user = UserInfo.objects.get(pk=id)
    # uname = request.session.get("user_name")
    # uaddress = request.GET.get("uaddress")
    # uphone = user.uphone
    # context = {"uname": uname, "uaddress": uaddress, "uphone": uphone}
    # print(uname,uaddress,uphone)#9.利用print调试，机智的boy
    if request.method=="POST":
        user.receiver = request.POST.get("receiver")#10.注意标签name value 要严格对应
        user.postcode = request.POST.get("postcode")
        user.uphone = request.POST.get("uphone")
        user.uaddress = request.POST.get("uaddress")
        user.save()                 #10.加了新功能撒
    context = {"user": user, "page_name": 3, "user_name": user_name,}
    return render(request,"df_user/user_center_site.html",context)

def logout(request):
    request.session.flush()#11.删除当前的会话数据并删除会话的Cookie
    url = request.COOKIES["url"]
    response = HttpResponseRedirect(url)
    # response.delete_cookie("sessionid")
    print("logout-url",url,request.COOKIES["sessionid"])

    return response