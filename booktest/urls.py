from django.conf.urls import include, url
from booktest import views  # 导入视图views

urlpatterns = [
    url(r'^index$', views.index),  # 首页
    # url(r'^showarg(\d+)$', views.show_args)  # 捕获url参数：位置参数,前面的组的值传给后面视图
    url(r'^showarg(?P<num>\d+)$', views.show_args),  # 捕获url参数：关键字参数,前面的组的值传给后面视图
    # 关键字参数，视图中参数名必须和正则表达式组名一致.
    url(r'^login$', views.login),
    url(r'^login_check$', views.login_check),  # 用户登录校验
]
