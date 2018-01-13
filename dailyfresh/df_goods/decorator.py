from django.http import HttpResponseRedirect,HttpResponse
from django.template import loader


def check_login(func):
    def inner(request,*args,**kwargs):
        if request.session.has_key("user_id"):
            print("has_key")
            return func(request,*args,**kwargs)

        else:
            red =HttpResponseRedirect("/user/login/")
            red.set_cookie("url", request.get_full_path())
            print("redict")
            return red
    return inner
def coat(context):
    def register_url(func):
        def inner(request,*args,**kwargs):
            t1 = loader.get_template('df_goods/%s.html'%func)

            response = HttpResponse(t1.render(context))

            url = request.get_full_path()
            response.set_cookie("url", value=url)


            return func(request, *args, **kwargs)

        return inner
    return register_url