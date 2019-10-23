from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response


# Create your views here.
# 视图的参数request就是HttpRequest类型的对象
# request包含浏览器请求的信息
def index(request):
    print(request.method)
    return render(request, 'booktest/index.html')


def page_not_found(request):
    return render_to_response('404page.html')


def page_error(request):
    return render_to_response('500.html')


def show_args(request, num):
    # 数字返回
    return HttpResponse(num)
    # 关键字参数，视图中参数名必须和正则表达式组名一致.


def login(request):
    return render(request, 'booktest/login.html')


def login_check(request):
    # 登录校验视图
    # 1 获取提交的用户名和密码
    # POST和GET对应提交的方式,都是QueryDict类型的对象
    print(request.method)
    print(type(request.POST))  # <class 'django.http.request.QueryDict'>

    username = request.POST.get('username')
    password = request.POST.get('password')  # 有输出
    print(username, password)
    # 2 进行登录的校验。模拟 hu  666
    if username == 'hu' and password == '666':
        # 用户名密码正确，跳转首页
        return redirect('/index')
    else:
        # 跳转登录页面
        return redirect('/login')

    # 3 返回应答
    # return HttpResponse('OK login_check')


'''
>>> from django.http.request import QueryDict
>>> QueryDict('a=1&b=2&c=3')
<QueryDict: {'a': ['1'], 'b': ['2'], 'c': ['3']}>
>>> q =QueryDict('a=1&b=2&c=3')
>>> q['a']
'1'
>>> q.get('a')
'1'
'''
