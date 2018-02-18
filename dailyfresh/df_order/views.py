from django.shortcuts import render, redirect
from django.db import transaction
from django.http import JsonResponse
from datetime import datetime
from decimal import Decimal

from .models import *
from df_goods.models import *
from df_cart.models import *
from df_user.models import *
from df_user.user_decorator import check_login

# Create your views here.

@check_login
def order(request):
    user_id = request.session.get("user_id")
    user = UserInfo.objects.get(pk=user_id)
    cart_ids1 = request.GET.getlist("cart_id")
    cart_ids = [int(item) for item in cart_ids1]
    carts = CartInfo.objects.filter(pk__in=cart_ids)
    # print("carts",carts)
    cart_ids1 = ",".join(cart_ids1)
    print("i'm order",cart_ids1)
    context = {"user_name": user.uname,
               "user":user, "cart1": carts,
               "cart_ids":cart_ids1,
               }
    return render(request,"df_order/place_order.html",context)


@transaction.atomic()
@check_login
def order_handle(request):

    tran_pot = transaction.savepoint()
    cart_ids = request.POST.get("cart_ids")
    print("order_handle",cart_ids)
    print("total",request.POST.get("total"))
    try:
        now = datetime.now()
        user_id = request.session.get("user_id")
        user = UserInfo.objects.get(pk=user_id)
        # 订单
        order = OrderInfo()
        order.id = "%s%d"%(now.strftime("%Y%m%d%H%M%S"),user_id)
        print(type(user_id))
        order.user = user
        order.date = now
        order.total = Decimal(request.POST.get("total"))
        order.save()
        # 详单
        cart_ids = [int(item) for item in cart_ids.split(",")]
        print("for-start")
        for cart_id in cart_ids:
            detail = OrderDetailInfo()
            detail.order = order

            cart = CartInfo.objects.get(pk=cart_id)
            goods = cart.goods
            if goods.stocks>cart.count:
                print("if-start")
                goods.stocks-=cart.count
                goods.sales+=cart.count
                goods.save()

                # 订单可以达成完善详单
                detail.goods = goods
                detail.count = cart.count
                detail.price = goods.price
                detail.save()

                # 付款的商品要从购物车删除
                cart.delete()
                print("if-ok")
            else:
                transaction.rollback(tran_pot)
                print("transaction.rollback")
                return redirect("/cart/")
        print("transaction.savepoint_commit")
        transaction.savepoint_commit(tran_pot)

    except Exception as e:
        print("=*20%s"%e)
        transaction.savepoint_rollback(tran_pot)
    data = {"ok": 1}
    return JsonResponse(data)

def buy_now(request,count):
    now = datetime.now()
    user_id = request.session.get("user_id")
    user = UserInfo.objects.get(pk=user_id)

