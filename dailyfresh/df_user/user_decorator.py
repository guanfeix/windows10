from django.http import HttpResponseRedirect


def check_login(func):
    def inner(request,*args,**kwargs):
        if request.session.has_key("user_id"):
            print("check_in pass")
            return func(request,*args,**kwargs)

        else:
            red =HttpResponseRedirect("/user/login/")
            red.set_cookie("url", request.get_full_path())
            #为什么每次提取url都是user/info 因为只写了一次在请求用户中心（我只做了这个接口在html上）
            #这也解释了为啥每次都会redirect 到登陆页因为访问无权的用户信息也被重定向
            print("redict")
            return red
    return inner
