from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.paginator import Paginator
# Create your views here.
from .decorator import coat

def index(request):

    # new_id1 = new[0].id
    # new_id2 = new[1].id
    # new_id3 = new[2].id
    # request.session["latest"]=new_id1
    # request.session["secondary"]=new_id2
    # goods_latest = GoodsInfo.objects.filter(pk=new_id1)
    # goods_secondary = GoodsInfo.objects.filter(pk=new_id2)
    # goods_third = GoodsInfo.objects.filter(pk=new_id3)
    user_name = request.session.get("user_name")
    classify= ClassifyInfo.objects.all()
    news = classify[0].goodsinfo_set.order_by("-pk")[0:3]#1.倒序加个-就行了
    fruit_04 = classify[0].goodsinfo_set.order_by("popularity")[0:5]
    list={"c1":classify}
    context={"title":"首页","list":list, "fruit_04":fruit_04,
             "goods_third": news[0],"goods_secondary": news[0],
             "goods_latest": news[0],"user_name":user_name
             }




    t1 = loader.get_template('df_goods/index.html')
    response = HttpResponse(t1.render(context))

    url = request.get_full_path()
    response.set_cookie("url", value=url)

    # return response
    # print(context["fruit_04"][3].title)
    return render(request,"df_goods/index.html",context)

def list(request,page_id,sort):
    user_name = request.session.get("user_name")
    id = request.GET.get("id")
    classify = ClassifyInfo.objects.filter(pk=id)
    if sort=='0':
        goods_list = classify[0].goodsinfo_set.order_by("-sales")
    elif sort=='1':
        goods_list = classify[0].goodsinfo_set.order_by("-price")
    elif sort == '2':
        goods_list = classify[0].goodsinfo_set.order_by("-popularity")
    paginator = Paginator(goods_list,10)
    page = paginator.page(int(page_id))
    print(page)

    id = request.GET.get("id")
    goods = GoodsInfo.objects.get(pk=id)
    news = goods.classify.goodsinfo_set.order_by("-pk")


    context = {"classify": classify[0], "goods_list": goods_list,
               "goods_latest": news[0], "sort":int(sort), "page":page,
               "goods_secondary": news[1], "paginator": paginator,
               "user_name": user_name,
               }
    # return render(request,"df_goods/list.html",context)
    t1 = loader.get_template('df_goods/list.html')
    response = HttpResponse(t1.render(context))

    url = request.get_full_path()
    response.set_cookie("url", value=url)

    return response

def detail(request):
    user_name = request.session.get("user_name")

    id = request.GET.get("id")
    goods = GoodsInfo.objects.get(pk=id)
    news = goods.classify.goodsinfo_set.order_by("-pk")
    goods.popularity += 1
    goods.save()
    context={"goods":goods,"classify":goods.classify,
             "goods_latest":news[0], "user_name": user_name,
             "goods_secondary": news[1]}
    # return render(request,"df_goods/detail.html",context)
    t1 = loader.get_template('df_goods/detail.html')
    response = HttpResponse(t1.render(context))

    url = request.get_full_path()
    response.set_cookie("url", value=url)

    return response