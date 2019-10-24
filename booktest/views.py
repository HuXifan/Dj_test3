from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render_to_response
from datetime import datetime, timedelta


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
    '''显示登录页面'''
    # 先判断用户是否登录
    if request.session.has_key('islogin'):
        # 用户已经登录，跳转首页
        return redirect('/index')
    else:
        # 用户没有登录
        # 获取登录cookie username
        if 'username' in request.COOKIES:
            # 如果Cookie丽有username，取值，取空
            username = request.COOKIES['username']
        else:
            username = ''
        return render(request, 'booktest/login.html', {'username': username})


def login_check(request):
    # 登录校验视图
    # 1 获取提交的用户名和密码
    # POST和GET对应提交的方式,都是QueryDict类型的对象
    print(request.method)
    print(type(request.POST))  # <class 'django.http.request.QueryDict'>

    username = request.POST.get('username')
    password = request.POST.get('password')  # 有输出
    remember = request.POST.get('remember')
    print(remember)
    print(username, password)
    # 2 进行登录的校验。模拟 hu  666
    if username == 'hu' and password == '666':
        # 用户名密码正确，跳转首页
        # 用户名和密码正确的时候判断是否需要记住户名密码
        response = redirect('/index')  # HttpResponse
        if remember == 'on':
            # response.set_cookie('username', username, max_age=7 * 24 * 3600)
            response.set_cookie('username', username, expires=datetime.now() + timedelta(days=14))
            # 设置usename过期时间为1周 Set-Cookie: username=hu; expires=Thu, 31-Oct-2019 08:19:29 GMT; Max-Age=604800
        # 记住用户登录状态
        request.session['islogin'] = True  # 只要有这个值就说明登录
        return response  # 设置好cookie后再应答
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


#
def ajax_test(request):
    # 显示Ajax页面
    return render(request, 'booktest/test_ajax.html')


def ajax_handle(request):
    # ajax请求处理
    # 返回json数据 {'res':1}
    # JsonResponse对象会把这个转化成Json数据返回给浏览器，由function(data)接受
    return JsonResponse({'res': 1})


# /login_ajax
def login_ajax(request):
    # 显示Ajax登录页面
    return render(request, 'booktest/login_ajax.html')


# /login_ajax_check
def login_ajax_check(request):
    # ajax 登录校验
    # 1 获取有用户名密码
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 2 进行校验，返回json数据
    if username == 'hu' and password == '666':
        # correct
        return JsonResponse({'res': 1})
        # Ajax请求在后台，不哟啊返回页面或者重定向
        # return redirect("/index")
    else:
        # 用户名或密码错误
        return JsonResponse({'res': 0})


# /set_session
def set_session(request):
    '''设置session'''
    request.session['username'] = 'hu'
    request.session['age'] = 18  # 以键值对的格式写session。
    request.session.set_expiry(None)
    return HttpResponse("设置session")


'''
如果value是一个整数，会话将在value秒没有活动后过期。
如果value为0，那么用户会话的Cookie将在用户的浏览器关闭时过期。
如果value为None，那么会话永不过期。
'''


# /get_session
def get_session(request):
    '''获取session，通过request.session'''
    username = request.session['username']
    age = request.session['age']  # 根据键读取值。
    return HttpResponse(username + ':' + str(age))  # age转换成字符串防止出错


def clear_session(request):
    # request.session.clear()  # 清除所有session，在存储中删除值部分。
    request.session.flush()  # 清除session数据，在存储中删除session的整条数据。
    return HttpResponse('清除session成功')
