"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from mlsx import views

urlpatterns = [
    url(r'^send_goods/', views.send_goods),
    url(r'^goods_info/', views.goods_info),
    url(r'^first_classify/', views.first_classify),
    url(r'^test/', views.test),
    url(r'^findbyname/', views.findbyname),
    url(r'^addtocart/', views.addtocart),
    url(r'^check_market/', views.check_market),
    url(r'^addcart/', views.addcart),
    url(r'^subcart/', views.subcart),
    url(r'^sort_goods/', views.sort_goods),
    url(r'^addUser/', views.addUser),
    url(r'^dredge_vip/', views.dredge_vip),
    url(r'^check_vip_time/', views.check_vip_time),
    url(r'^query_vip/', views.query_vip),
    url(r'^promotion_goods/', views.promotion_goods),
    url(r'^query_promotion_goods/', views.query_promotion_goods),
    url(r'^send_count_goods/', views.send_count_goods),
    url(r'^goods_select/', views.goods_select),
    url(r'^give_endtime_vip/', views.give_endtime_vip),
    url(r'^renew_vip/', views.renew_vip),
    url(r'^order/', views.order),
    url(r'^submit_order/', views.submit_order),
    url(r'^pay_goods/', views.pay_goods),
    url(r'^check_order/', views.check_order),
    # url(r'^change_order_status/', views.change_order_status),
    url(r'^morning_addtocart/', views.morning_addtocart),
    url(r'^receive_goods/', views.receive_goods),
    url(r'^evaluate_goods/', views.evaluate_goods),
    url(r'^check_isvip/', views.check_isvip),
    url(r'^send_pt_goods/', views.send_pt_goods),
    url(r'^start_team/', views.start_team),
    url(r'^join_team/', views.join_team),
    url(r'^send_isstart_goods/', views.send_isstart_goods),
    url(r'^check_person/', views.check_person),
    url(r'^check_isdate/', views.check_isdate),
    url(r'^query_order/', views.query_order),
    url(r'^cancel_order/', views.cancel_order),
    url(r'^after_pay/', views.after_pay),
    url(r'^pt_order/', views.pt_order),
    url(r'^pt_pay/', views.pt_pay),
    url(r'^delete_team/', views.delete_team),
    url(r'^open_team/', views.open_team),

]
