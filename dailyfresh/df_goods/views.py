from django.shortcuts import render
from .models import *
from datetime import date

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.paginator import Paginator


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

    return response
    # print(context["fruit_04"][3].title)
    # return render(request,"df_goods/index.html",context)


def list1(request,page_id,sort):#3.不要用内建函数作为函数名日
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
    list_str = request.COOKIES.get("recent_list_str")


    if list_str is not None:
        recent_list =list_str.split(",")

        if str(id) not in recent_list:
            if len(recent_list)==5:
                recent_list.pop()
                # del recent_list[4]
                # recent_list = list(set(recent_list))
                #用序列好像失序了不能很好的控制顺序，这倒罢了但是不能替换最老的浏览这就是问题了
                # ,几经删减程序就很健壮了，不同的环境，耦合性会降低
        else:
            recent_list.remove(str(id))
        recent_list.insert(0, str(id))
        recent_list_str =",".join(recent_list)

    else:
        recent_list_str = str(id)

    print("recent_list_str", recent_list_str)
    response.set_cookie("recent_list_str",recent_list_str)

    return response


from haystack.views import SearchView


class FacetedSearchView(SearchView):
    def extra_context(self):

        extra = super(FacetedSearchView, self).extra_context()
        extra["title"] = "搜索"
        extra["user_name"] = "user_name"

        return extra


# from haystack.generic_views import SearchView
#
#
# class MySearchView(SearchView):
#     """My custom search view."""
#
#     def get_queryset(self):
#         queryset = super(MySearchView, self).get_queryset()
#         # further filter queryset based on some set of criteria
#         return queryset.filter(pub_date__gte=date(2015, 1, 1))
#
#     def get_context_data(self, *args, **kwargs):
#         extra = super(MySearchView, self).get_context_data(*args, **kwargs)
#
#         extra["title"] = "搜索"
#         extra["user_name"] = "user_name"
#         return extra
