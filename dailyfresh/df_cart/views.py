from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseRedirect
from .models import CartInfo
from df_goods.models import *
from df_user.models import *
from df_user.user_decorator import check_login
# Create your views here.


@check_login
def edit(request,cart_id,count):
    try:
        cart1 = CartInfo.objects.get(pk=int(cart_id))
        count1 = cart1.count
        cart1.count = int(count)
        cart1.save()
        data={"ok":0}
    except Exception as e:
        data = {"ok": count1}
    return JsonResponse(data)


@check_login
def delete(request,cart_id):
    try:
        cart1 = CartInfo.objects.get(pk=int(cart_id))
        cart1.delete()
        data={"ok":1}
    except Exception as e:
        data = {"ok": 0}
    return JsonResponse(data)


@check_login
def cart(request):
    user_name = request.session.get("user_name")
    user_id = request.session.get("user_id")
    cart1 = CartInfo.objects.filter(master=user_id)
    # goods_list = GoodsInfo.objects.get(pk=goods_id)
    context = {"user_name": user_name, "cart1": cart1}

    return render(request, "df_cart/cart.html", context)


@check_login
def buy(request,goods_id,count):
    user_id = request.session.get("user_id")
    goods = GoodsInfo.objects.get(pk=goods_id)
    master = UserInfo.objects.get(pk=user_id)

    cart1 = CartInfo()
    cart1.goods = goods
    cart1.master = master
    cart1.count = count
    cart1.save()

    cart2 = CartInfo.objects.filter(master=user_id).order_by("-pk")
    cart_id = cart2[0].id
    print("over")
    return redirect("/order/?cart_id=%d"%cart_id)

@check_login
def add(request,goods_id,count):
    user_id = request.session.get("user_id")

    if count=="0":
        print("count",count)
        count = CartInfo.objects.filter(master=user_id).count()
        return JsonResponse({"count": count})

    goods = GoodsInfo.objects.get(pk=goods_id)
    master = UserInfo.objects.get(pk=user_id)
    cart1 = CartInfo.objects.filter(goods=goods_id,master=user_id)
    # 这里有点东西逻辑有点理不清，购物车table里存的是一条条记录，并非想象中的容器，购物车是通过将同一用户的记录删选出来那购物车id有什么意义
    # 那个购物车，
    if len(cart1)>0:
        cart1 = cart1[0]
        cart1.count+=int(count)
        cart1.save()
        print(goods.title,"count",cart1.count)
    else:
        cart1 = CartInfo()
        cart1.goods = goods
        cart1.master = master
        cart1.count = count
        cart1.save()
    if request.is_ajax():
        count = CartInfo.objects.filter(master=user_id).count()
        return  JsonResponse({"count":count})
    return redirect("/cart/")
    # url = request.COOKIES["url"]
    # print("login-url", url)
    # return HttpResponseRedirect(url)