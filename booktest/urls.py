from django.conf.urls import include, url
from booktest import views  # 导入视图views

urlpatterns = [
    url(r'^index$', views.index),  # 首页

]
