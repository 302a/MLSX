import json
import re
import time
from datetime import datetime
from pprint import pprint

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.timezone import utc

from mlsx.models import food_goods, nofood_goods, fresh_goods, out_window_goods, fruit_goods, vegetable_goods, \
    dry_fruit_goods, meat_goods, Market, User, vip, morning_market, order_goods_list, order_list, goods_estimate, \
    pt_good, pt_list


def first_classify(request):
    data = {
        'status': '200',
        'msg': 'ok'
    }

    data['content'] = [{'type':'粮油副食'},{'type':'日常百货'},{'type':'精选生鲜'},{'type':'外场窗口'},
                       {'type':'新鲜水果'},{'type':'净菜蔬菜'},{'type':'坚果干货'},{'type':'肉禽蛋类'}]

    return JsonResponse(data)

def query_good(findtype,goods_type,find=None,findpara=None):
    goods_list = []
    if goods_type == '粮油副食':
        if findtype == 'all':
            goods_list = food_goods.objects.all()
        elif findtype == 'portion':
            if find == 'pk':
                goods_list = food_goods.objects.filter(pk=findpara)
            elif find == 'goodsType':
                goods_list = food_goods.objects.filter(goodsType=findpara)
    if goods_type == '日常百货':
        if findtype == 'all':
            goods_list = nofood_goods.objects.all()
        elif findtype == 'portion':
            if find == 'pk':
                goods_list = nofood_goods.objects.filter(pk=findpara)
            elif find == 'goodsType':
                goods_list = nofood_goods.objects.filter(goodsType=findpara)
    if goods_type == '精选生鲜':
        if findtype == 'all':
            goods_list = fresh_goods.objects.all()
        elif findtype == 'portion':
            if find == 'pk':
                goods_list = fresh_goods.objects.filter(pk=findpara)
            elif find == 'goodsType':
                goods_list = fresh_goods.objects.filter(goodsType=findpara)
    if goods_type == '外场窗口':
        if findtype == 'all':
            goods_list = out_window_goods.objects.all()
        elif findtype == 'portion':
            if find == 'pk':
                goods_list = out_window_goods.objects.filter(pk=findpara)
            elif find == 'goodsType':
                goods_list = out_window_goods.objects.filter(goodsType=findpara)
    if goods_type == '新鲜水果':
        if findtype == 'all':
            goods_list = fruit_goods.objects.all()
        elif findtype == 'portion':
            if find == 'pk':
                goods_list = fruit_goods.objects.filter(pk=findpara)
            elif find == 'goodsType':
                goods_list = fruit_goods.objects.filter(goodsType=findpara)
    if goods_type == '净菜蔬菜':
        if findtype == 'all':
            goods_list = vegetable_goods.objects.all()
        elif findtype == 'portion':
            if find == 'pk':
                goods_list = vegetable_goods.objects.filter(pk=findpara)
            elif find == 'goodsType':
                goods_list = vegetable_goods.objects.filter(goodsType=findpara)
    if goods_type == '坚果干货':
        if findtype == 'all':
            goods_list = dry_fruit_goods.objects.all()
        elif findtype == 'portion':
            if find == 'pk':
                goods_list = dry_fruit_goods.objects.filter(pk=findpara)
            elif find == 'goodsType':
                goods_list = dry_fruit_goods.objects.filter(goodsType=findpara)
    if goods_type == '肉禽蛋类':
        if findtype == 'all':
            goods_list = meat_goods.objects.all()
        elif findtype == 'portion':
            if find == 'pk':
                goods_list = meat_goods.objects.filter(pk=findpara)
            elif find == 'goodsType':
                goods_list = meat_goods.objects.filter(goodsType=findpara)

    return goods_list

def send_goods(request):
    data = {
        'status': '200',
        'msg': 'ok',
    }

    dic1 = {}
    dic2 = {}

    # 获取从前端传回的商品类型
    goods_type = request.GET.get('type')

    goods_list = query_good('all',goods_type)

    good_type_list = []
    for info in goods_list:
        if info.goodsType not in good_type_list:
            good_type_list.append(info.goodsType)

    dic_list = []
    for n in range(len(good_type_list)):
        dic_list.append(n)
        good_object = query_good('portion',goods_type,find='goodsType',findpara=good_type_list[n])
        dic2[good_type_list[n]] = list(good_object.values())

        dic_list[n] = {
            'goodstype': good_type_list[n],
            'goods': dic2[good_type_list[n]],
            'id': n + 1,
        }

    data['content'] = dic_list

    return JsonResponse(data)

def goods_info(request):
    goodsid = request.GET.get('goodsid')
    goodtype = request.GET.get('goodtype')

    goods = query_good('portion',goodtype,find='pk',findpara=goodsid)

    data = {
        'status': '200',
        'msg': 'ok',
    }
    data['content'] = list(goods.values())

    return JsonResponse(data)

def test(request):
    data = {
        'status': '200',
        'msg': 'ok'
    }

    a = food_goods
    info = a.objects.all()
    # print(info)

    return JsonResponse(data)

def findby(goodsname):
    goods_list = food_goods.objects.filter(goodsname__contains=goodsname)

    if not goods_list.exists():
        goods_list = nofood_goods.objects.filter(goodsname__contains=goodsname)

    if not goods_list.exists():
        goods_list = fresh_goods.objects.filter(goodsname__contains=goodsname)

    if not goods_list.exists():
        goods_list = out_window_goods.objects.filter(goodsname__contains=goodsname)

    if not goods_list.exists():
        goods_list = fruit_goods.objects.filter(goodsname__contains=goodsname)

    if not goods_list.exists():
        goods_list = vegetable_goods.objects.filter(goodsname__contains=goodsname)

    if not goods_list.exists():
        goods_list = dry_fruit_goods.objects.filter(goodsname__contains=goodsname)

    if not goods_list.exists():
        goods_list = meat_goods.objects.filter(goodsname__contains=goodsname)

    return goods_list


def findbyname(request):
    goodsname = request.GET.get('goodsname')
    data = {}

    goods_list = findby(goodsname)

    if not goods_list.exists():
        data['status'] = '404'
        data['msg'] = '不存在此商品'

    else:
        data['status'] = '200'
        data['msg'] = 'ok'
        data['content'] = list(goods_list.values())

    return JsonResponse(data)

# 将商品添入购物车的接口
def addtocart(request):
    goodid = request.GET.get('goodid')
    goods_type = request.GET.get('type')
    data = {}

    # 获取用户信息
    userid = request.GET.get('userid')

    if goods_type == '拼团商品':
        goodlist = pt_good.objects.filter(pk=goodid)
    else:
        # 根据商品编号查找商品
        goodlist = query_good('portion',goods_type,find='pk',findpara=goodid)

    if userid != None:
        if goodlist.exists():
            good = goodlist.first()

            # 判断购物车是否已经有此商品
            markets = Market.objects.filter(userid=userid).filter(goodsid=goodid)

            if markets.exists():
                market = markets.first()
                count = int(market.buycount)
                market.buycount = str(count + 1)

                market.save()
                data['status'] = '200'
                data['msg'] = '已成功添加到购物车中'

            else:
                # 将对应信息添加到购物车表中
                market = Market()
                market.userid = userid
                market.goodsid = good.id
                market.buycount = '1'
                market.isselect = 'true'
                market.is_morning = 'false'
                if goods_type == '拼团商品':
                    market.goods_price = good.price
                else:
                    market.goods_price = good.retail_price
                if goods_type == '拼团商品':
                    market.goods_vip_price = good.price
                else:
                    market.goods_vip_price = good.vip_price
                market.goodstype = goods_type

                market.save()
                data['status'] = '200'
                data['msg'] = '已成功添加到购物车中'

        else:
            data['status'] = '404'
            data['msg'] = '商品不存在'
    else:
        data['status'] = '300'
        data['msg'] = '用户请先登录'

    return JsonResponse(data)

# 合并商品数据库信息
def merge_info(goodlist):
    pass

# 购物车逻辑
def check_market(request):
    userid = request.GET.get('userid')
    data = {}
    goodlist = []

    # 判断购物车的早市商品是否超过早市时间
    morning_list = Market.objects.filter(userid=userid).filter(is_morning='true')
    timenow = datetime.now().replace(tzinfo=utc)
    for morning in morning_list:
        if int(time.mktime(timenow.timetuple())) - int(time.mktime(morning.pt_end_time.timetuple())) >= 0:
            goods = findby(morning.goodsid)
            if goods.exists():
                good = goods.first()
                morning.goodsid = good.id
                morning.goods_price = good.retail_price
                morning.goods_vip_price = good.vip_price

                morning.save()

            else:
                # 从购物车中删除此商品
                morning.delete()

    # 从购物车表中查询用户购买的商品
    # print(userid)
    goods_list = Market.objects.filter(userid=userid)

    if goods_list.exists():
        for n in range(len(goods_list)):
            id = goods_list[n].goodsid
            gtype = goods_list[n].goodstype

            market = list(goods_list.values())
            if gtype == '拼团商品':
                goodss = pt_good.objects.filter(pk=id)
            else:
                goodss = query_good('portion',gtype,find='pk',findpara=id)

            if goodss.exists():
                goodsinfo = list(goodss.values())[0]
                goods_info = dict(goodsinfo,**market[n])

                goodlist.append(goods_info)

            else:
                data['status'] = '404'
                data['msg'] = '出现未知错误'

        # print(goodlist)
        data['status'] = '200'
        data['msg'] = 'ok'
        data['content'] = goodlist

    else:
        data['status'] = '405'
        data['msg'] = '用户未添加任何商品到购物车'

    return JsonResponse(data)

# 分类页面加减数据
def addcart(request):
    goodid = request.GET.get('goodid')
    userid = request.GET.get('userid')
    goods_type = request.GET.get('type')
    data = {}

    markets = Market.objects.filter(userid=userid).filter(pk=goodid)

    if markets.exists():
        # 获取当前加入购物车的数量
        market = markets.first()
        count = int(market.buycount)
        market.buycount = str(count + 1)
        data['status'] = '200'
        data['msg'] = 'ok'

        market.save()

    else:
        goodlist = query_good('portion', goods_type, find='pk', findpara=goodid)

        # 将对应信息添加到购物车表中
        if goodlist.exists():
            good = goodlist.first()

            # 将对应信息添加到购物车表中
            market = Market()
            market.userid = userid
            market.goodsid = good.id
            market.buycount = '1'
            market.isselect = '1'

            market.save()
            data['status'] = '200'
            data['msg'] = '商品已添加到购物车中'

    return JsonResponse(data)

def subcart(request):
    goodid = request.GET.get('goodid')
    userid = request.GET.get('userid')
    goods_type = request.GET.get('type')
    data = {}
    print(goodid,userid)
    markets = Market.objects.filter(userid=userid).filter(pk=goodid)

    market = markets.first()
    # 获取当前加入购物车的数量
    count = market.buycount
    print(market)
    if count == '1':
        market.delete()

        data['status'] = '201'
        data['msg'] = '商品已从购物车删除'

    else:
        market.buycount = int(count) - 1
        market.save()

        data['status'] = '200'
        data['msg'] = 'ok'

    return JsonResponse(data)

# 根据条件排序
def sort_goods(request):
    sort_type = request.GET.get('sort_type')
    goodstype = request.GET.get('type')

    data = {}
    dic2 = {}
    goodslist = []

    if sort_type == '综合':
        goodslist = query_good('all',goodstype)
        data['content'] = list(goodslist.values())

    elif sort_type == '最新':
        pass

    elif sort_type == '价格升序':
        goods_list = query_good('all', goodstype)

        good_type_list = []
        for info in goods_list:
            if info.goodsType not in good_type_list:
                good_type_list.append(info.goodsType)

        dic_list = []
        for n in range(len(good_type_list)):
            dic_list.append(n)
            good_object = query_good('portion', goodstype, find='goodsType', findpara=good_type_list[n]).order_by(
                'retail_price')
            dic2[good_type_list[n]] = list(good_object.values())

            dic_list[n] = {
                'goodstype': good_type_list[n],
                'goods': dic2[good_type_list[n]],
                'id': n + 1,
            }

        data['content'] = dic_list

    elif sort_type == '价格降序':
        goods_list = query_good('all', goodstype)

        good_type_list = []
        for info in goods_list:
            if info.goodsType not in good_type_list:
                good_type_list.append(info.goodsType)

        dic_list = []
        for n in range(len(good_type_list)):
            dic_list.append(n)
            good_object = query_good('portion', goodstype, find='goodsType', findpara=good_type_list[n]).order_by('-retail_price')
            dic2[good_type_list[n]] = list(good_object.values())

            dic_list[n] = {
                'goodstype': good_type_list[n],
                'goods': dic2[good_type_list[n]],
                'id': n + 1,
            }

        data['content'] = dic_list


    elif sort_type == '销量':
        pass

    data['status'] = '200'
    data['msg'] = 'ok'

    return JsonResponse(data)

# 购物车商品选中,取消接口
def goods_select(request):
    select = request.GET.get('select')
    userid = request.GET.get('userid')
    goodid = request.GET.get('id')
    data = {}

    marketlist = Market.objects.filter(userid=userid).filter(goodsid=goodid)

    if marketlist.exists():
        market = marketlist.first()
        if select == 'true':
            market.isselect = 'true'
            market.save()
            data['status'] = '200'
            data['msg'] = 'ok'
        elif select == 'false':
            market.isselect = 'false'
            market.save()
            data['status'] = '200'
            data['msg'] = 'ok'

    return JsonResponse(data)

def addUser(request):
    userid = request.GET.get('userid')
    data = {}

    # 判断用户是否在用户表中
    userlist = User.objects.filter(openid=userid)

    if userlist.exists():
        data['status'] = '300'
        data['msg'] = '用户已存在'

    else:
        user = User()
        user.openid = userid

        user.save()
        data['status'] = '200'
        data['msg'] = '用户保存成功'

    return JsonResponse(data)

# 将开通时间转换成天数
def change_day(time):
    if time == '1':
        time = '一个月'
    elif time == '3':
        time = '三个月'
    elif time == '6':
        time = '六个月'
    elif time == '12':
        time = '一年'

    # 从数据库中查询vip天数
    viplist = vip.objects.filter(viptime=time)

    if viplist.exists():
        vips = viplist.first()
        vipdays = vips.days
        viptypes = vips.viptype

    return vipdays,viptypes

# 开通会员
def dredge_vip(request):
    userid = request.GET.get('userid')

    userlist = User.objects.filter(openid=userid)
    data = {}
    # 获取会员开通时间
    viptime = request.GET.get('viptime')

    vipdays,viptypes = change_day(viptime)

    if userlist.exists():
        users = userlist.first()
        from datetime import datetime
        timenow = datetime.now().replace(tzinfo=utc)
        users.vip_start_time = timenow
        import datetime
        # print(timenow + datetime.timedelta(days=90),type(timenow + datetime.timedelta(days=90)))
        users.vip_end_time = timenow + datetime.timedelta(days=int(vipdays))
        users.vipid = users.id
        users.userType = viptypes

        users.save()
        data['status'] = '200'
        data['msg'] = '开通成功'
    else:
        users = User()
        users.openid = userid
        from datetime import datetime
        timenow = datetime.now().replace(tzinfo=utc)
        users.vip_start_time = timenow
        import datetime
        users.vip_end_time = timenow + datetime.timedelta(days=int(vipdays))
        # 获取最后一个用户id并加一
        userss = User.objects.all()
        finuser = userss.last()

        users.vipid = finuser.id
        users.userType = viptypes

        users.save()
        data['status'] = '200'
        data['msg'] = '添加并开通成功'

    return JsonResponse(data)

# 返回会员到期时间
def give_endtime_vip(request):
    userid = request.GET.get('userid')

    data = {}

    userlist = User.objects.filter(openid=userid)
    if userlist.exists():
        user = userlist.first()
        data['status'] = '200'
        data['msg'] = 'ok'
        time = str(user.vip_end_time)

        data['expire'] = time[:10]
        # print('发送成功')

    else:
        data['status'] = '300'
        data['msg'] = '用户未登录'
        # print('用户未登录')

    return JsonResponse(data)

# 续费会员
def renew_vip(request):
    userid = request.GET.get("userid")

    userlist = User.objects.filter(openid=userid)
    data = {}
    # 获取会员开通时间
    viptime = request.GET.get('viptime')

    vipdays, viptypes = change_day(viptime)

    try:
        user = userlist.first()
        after_endtime = user.vip_end_time
        import datetime
        user.vip_end_time = after_endtime + datetime.timedelta(days=int(vipdays))

        user.save()
        data['status'] = '200'
        data['msg'] = '续费成功'

        return JsonResponse(data)
    except Exception as e:
        # print(e)
        data['status'] = '300'
        data['msg'] = '发生未知错误'
        return JsonResponse(data)

# 查询会员对应规则
def query_vip(request):
    viplist = vip.objects.all()
    data = {}
    vip_list = []

    vip_type_list = []
    for info in viplist:
        if info.viptime not in vip_type_list:
            vip_type_list.append(info.viptime)

    for vip_type in vip_type_list:
        vip_object = vip.objects.filter(viptime=vip_type)
        viplist.append({
            'type': vip_type,
            'content': list(vip_object.values())
        })

    data['status'] = '200'
    data['msg'] = 'ok'
    data['content'] = vip_list

    return JsonResponse(data)

# 判断用户是否是会员
def check_isvip(request):
    userid = request.GET.get('userid')
    data = {}

    userlist = User.objects.filter(openid=userid)

    try:
        user = userlist.first()
        data['status'] = '200'
        data['msg'] = 'ok'
        data['content'] = user.userType

        return JsonResponse(data)
    except Exception as e:
        data['status'] = '303'
        data['msg'] = '发生未知错误'
        return JsonResponse(data)

# 判断会员是否过期
def check_vip_time(request):
    data = {}

    # 获取当前打开页面时间
    timenow = datetime.now().replace(tzinfo=utc)
    # 获取会员结束时间
    userid = request.GET.get('userid')

    userlist = User.objects.filter(openid=userid)
    if userlist.exists():
        user = userlist.first()
        vip_end_time = user.vip_end_time

        result = int(time.mktime(timenow.timetuple())) - int(time.mktime(vip_end_time.timetuple()))
        if result >= 0:
            data['status'] = '300'
            data['msg'] = '会员已过期'
            user.userType = '普通会员'
            user.vipid = None

            user.save()
        else:
            data['status'] = '200'
            data['msg'] = '会员未过期'

    else:
        data['status'] = '404'
        data['msg'] = '用户未开通会员'

    return JsonResponse(data)

# 获取早市商品
def promotion_goods(request):
    morning = morning_market.objects.all()

    data = {
        'status': '200',
        'msg': 'ok',
        'content': list(morning.values())
    }

    return JsonResponse(data)

# 查询单个早市商品
def query_promotion_goods(request):
    goodid = request.GET.get('goodid')
    data = {}
    goodlist = morning_market.objects.filter(pk=goodid)

    if goodlist.exists():
        data['status'] = '200'
        data['msg'] = 'ok'
        data['content'] = list(goodlist.values())

    else:
        data['status'] = '404'
        data['msg'] =[ '商品不存在']

    return JsonResponse(data)

# 早市商品添加到购物车
def morning_addtocart(request):
    goodid = request.GET.get('goodid')
    userid = request.GET.get('userid')
    data = {}

    goodlist = morning_market.objects.filter(pk=goodid)

    if userid != None:
        if goodlist.exists():
            good = goodlist.first()

            # 将对应信息添加到购物车表中
            market = Market()
            market.userid = userid
            market.goodsid = good.goodname
            market.buycount = '1'
            market.isselect = 'true'
            market.is_morning = 'true'
            market.goods_price = good.retail_price
            market.goods_vip_price = good.vip_price

            market.save()
            data['status'] = '200'
            data['msg'] = '已成功添加到购物车中'

        else:
            data['status'] = '404'
            data['msg'] = '商品不存在'
    else:
        data['status'] = '300'
        data['msg'] = '用户请先登录'

    return JsonResponse(data)

# 根据个数及类型获取商品
def send_count_goods(request):
    count = request.GET.get('count')
    goodtype = request.GET.get('goodtype')

    goodlist = query_good('all',goodtype)
    data = {}
    if len(goodlist) >= int(count):
        goods = list(goodlist.values())
        data['stauts'] = '200'
        data['msg'] = 'ok'
        data['content'] = goods[0:int(count)]
        data['type'] = goodtype

    else:
        data['stauts'] = '300'
        data['msg'] = '没有这么多商品'

    return JsonResponse(data)

# 订单页面接口
def order(request):
    userid = request.GET.get("userid")

    # 获取前端计算出来的总价
    # total_price = request.GET.get('total_price')
    data = {}
    marketlist = []

    # 从购物车中找出已选中的商品
    market_list = Market.objects.filter(userid=userid).filter(isselect='true')

    if market_list.exists():
        for n in range(len(market_list)):
            id = market_list[n].goodsid
            gtype = market_list[n].goodstype
            market = list(market_list.values())
            if market_list[n].is_morning == 'true':
                goodss = morning_market.objects.filter(pk=id)
            else:
                goodss = query_good('portion',gtype,find='pk',findpara=id)
            if gtype == '拼团商品':
                goodss = pt_good.objects.filter(pk=id)
            if goodss.exists():
                goodsinfo = list(goodss.values())[0]
                goods_info = dict(goodsinfo,**market[n])

                marketlist.append(goods_info)

            else:
                data['status'] = '404'
                data['msg'] = '出现未知错误'

        data['status'] = '200'
        data['msg'] = 'ok'
        data['content'] = marketlist

    else:
        data['status'] = '404'
        data['msg'] = '未添加任何商品到购物车'

    return JsonResponse(data)

# 将时间戳转换为字符串加上id作为ordernum
def exchange_time(time,id):
    time_list = []
    time_list.append(str(time.year))
    time_list.append(str(time.month))
    time_list.append(str(time.day))
    time_list.append(str(time.hour))
    time_list.append(str(time.minute))
    time_list.append(str(time.second))

    times = ''
    for i in time_list:
        times += i

    order_num = times + str(id)

    return order_num

# 数据处理
def data_dispose(goods):
    mode1 = re.compile('"id":(\d+)')
    result1 = mode1.search(goods)
    change1 = result1.group().split(':')
    id = change1[-1]
    print(id)
    mode2 = re.compile('"goodstype":"(\w+)"')
    result2 = mode2.search(goods)
    if result2 == None:
        goodstype = None
    else:
        change2 = result2.group().split(':')
        goodstype = change2[-1][1:-1]
    print(goodstype)
    mode3 = re.compile('"buycount":"(\d+)"')
    result3 = mode3.search(goods)
    if result3 == None:
        goods_num = None
    else:
        change3 = result3.group().split(':')
        goods_num = change3[-1][1:-1]
    print(goods_num)
    mode4 = re.compile('"retail_price":"(.*?)"')
    result4 = mode4.search(goods)
    if result4 == None:
        goodsprice = None
    else:
        change4 = result4.group().split(':')
        goodsprice = change4[-1][1:-1]
    print(goodsprice)
    return id,goodstype,goods_num,goodsprice

# 提交订单接口
def submit_order(request):
    data = {}

    userid = request.POST.get('userid')

    goodsinfo = request.POST.get('goodsinfo')
    info_str = goodsinfo[1:-1]
    info_list = info_str.split('},')

    markets1 = Market.objects.filter(userid=userid)
    for market in markets1:
        market.isselect = 'false'
        market.save()
    try:
        for goods in info_list:
            id,goodstype,goods_num,goodsprice = data_dispose(goods)
            print(id,goodstype,goods_num,goodsprice)

            markets = Market.objects.filter(userid=userid).filter(goodstype=goodstype)

            if markets.exists():
                marketss = markets.filter(pk=id)
            else:
                continue

            if marketss.exists():
                market = marketss.first()
                market.isselect = 'true'

                market.save()

        data['status'] = '200'
        data['msg'] = 'ok'

        return JsonResponse(data)

    except Exception as e:
        data['status'] = '300'
        data['msg'] = '出现异常错误'

        return JsonResponse(data)

# 立即支付接口
def pay_goods(request):
    data = {}

    userid = request.POST.get('userid')
    remark = request.POST.get('remark')
    pay_price = request.POST.get('pay_price')
    receive_addr = request.POST.get('receive_addr')
    need_pay_price = request.POST.get('need_pay_price')
    goodsinfo = request.POST.get('goodsinfo')
    info_str = goodsinfo[1:-1]
    info_list = info_str.split('},')
    print(goodsinfo)
    # 获取id
    users = User.objects.filter(openid=userid)
    user = users.first()
    id = user.id
    import datetime
    timenow = datetime.datetime.now()

    if remark == 'undefined':
        remark = 'none'

    # 生成订单号
    order_num = exchange_time(timenow, id)
    print(order_num)
    try:
        # 生成订单
        orderlist = order_list()
        orderlist.order_number = order_num
        orderlist.userid = userid
        orderlist.is_pay = 'false'
        orderlist.is_ship = 'false'
        orderlist.is_receipt = 'false'
        orderlist.status = '待付款'
        orderlist.need_pay_price = need_pay_price
        orderlist.pay_price = pay_price
        orderlist.receive_addr = receive_addr
        orderlist.remark = remark
        from datetime import  datetime
        timenow = datetime.now().replace(tzinfo=utc)
        orderlist.create_time = timenow

        orderlist.save()
        # 生成订单表
        for goods in info_list:
            id, goodstype, goods_num, goodsprice = data_dispose(goods)

            mode5 = re.compile('"goodsid":"(\d+)"')
            result5 = mode5.search(goods)
            change5 = result5.group().split(':')
            goodsid = change5[-1][1:-1]
            print(goodsid)
            markets = Market.objects.filter(pk=id)
            market = markets.first()
            market.delete()

            # 判断商品是否是早市
            mode2 = re.compile('"is_morning":"(\w+)"')
            result2 = mode2.search(goods)
            change2 = result2.group().split(':')
            is_morning = change2[-1][1:-1]
            print(is_morning)
            if is_morning == 'true':
                goodstype = '促销商品'
            print('-------------------',goodstype,goodsid,goods_num,goodsprice,userid,order_num)
            order = order_goods_list()
            order.goodsid = goodsid
            order.goodstype = goodstype
            order.goods_num = goods_num
            order.goodsprice = goodsprice
            order.userid = userid
            order.order_number = order_num
            order.is_estimate = 'false'
            timenow = datetime.now().replace(tzinfo=utc)
            order.create_time = timenow

            order.save()

        data['status'] = '200'
        data['msg'] = 'ok'
        data['content'] = order_num
        print(data['content'])
        return JsonResponse(data)

    except Exception as e:
        data['status'] = '300'
        data['msg'] = '出现异常错误'

        return JsonResponse(data)

# 支付接口
def after_pay(request):
    order_num = request.GET.get('order_num')
    userid = request.GET.get('userid')
    data = {}

    orderlist = order_list.objects.filter(order_number=order_num).filter(userid=userid)

    timenow = datetime.now().replace(tzinfo=utc)
    try:
        order = orderlist.first()
        order.status = "待配送"
        order.is_pay = 'true'
        order.pay_time = timenow

        order.save()
        data['status'] = '200'
        data['msg'] = '待发货'

        return JsonResponse(data)

    except Exception:
        data['status'] = '300'
        data['msg'] = '发生异常,支付失败'
        return JsonResponse(data)

# 查看订单状态
# def check_goods_status(request):
#     order_num = request.GET.get('order_num')
#     data = {}
#
#     orderlist = order_list.objects.filter(order_number=order_num)
#     if orderlist.exists():
#         pass
#
#     else:
#         data['status'] = '404'
#         data['msg'] = '订单号不存在'

# 商品评价功能
def evaluate_goods(request):
    order_num = request.GET.get('order_num')
    userid = request.GET.get('userid')
    estimate_type = request.GET.get('estimate_type')
    goods_descripe = request.GET.get('goods_descripe')
    send_server = request.GET.get('send_server')
    server_attitute = request.GET.get('server_attitute')
    data = {}

    try:
        estimate = goods_estimate()
        estimate.estimate_type = estimate_type
        estimate.goods_descripe = goods_descripe
        estimate.send_server = send_server
        estimate.server_attitute = server_attitute
        estimate.userid = userid
        estimate.order_number = order_num

        estimate.save()
        data['status'] = '200'
        data['msg'] = '评价成功'
        return JsonResponse(data)
    except Exception as e:
        data['status'] = '300'
        data['msg'] = '发生异常错误'

        return JsonResponse(data)

# 收货接口
def receive_goods(request):
    order_num = request.GET.get('order_num')
    orderlist = order_list.objects.filter(order_number=order_num)
    data = {}

    try:
        order = orderlist.first()
        order.is_receipt = 'true'
        order.status = '待评价'
        timenow = datetime.now().replace(tzinfo=utc)
        order.receipt_time = timenow

        order.save()
        data['status'] = '200'
        data['msg'] = '收货成功'
        return JsonResponse(data)

    except Exception as e:
        data['status'] = '300'
        data['msg'] = '发生异常错误'
        return JsonResponse(data)

# 查看订单
def check_order(request):
    userid = request.GET.get('userid')
    status = request.GET.get('status')
    data = {}
    order_lists = []

    finally_list = []

    orderlists = order_list.objects.filter(userid=userid)
    if orderlists.exists():
        if status == '全部订单':
            orderlist = orderlists
        else:
            orderlist = orderlists.filter(status=status)
        # 获取所有订单号
        for i in orderlist:
            order_lists.append(i.order_number)

        # 根据订单号去订单商品表查询商品
        for j in order_lists:
            good_info_list = []
            order_goods = order_goods_list.objects.filter(order_number=j)
            order_goodss = pt_list.objects.filter(order_number=j)
            print(order_goodss)
            count = 0
            for n in range(len(order_goods)):
                id = order_goods[n].goodsid
                gtype = order_goods[n].goodstype
                goods_num = order_goods[n].goods_num

                count += int(goods_num)

                order_info = list(order_goods.values())
                if gtype == '拼团商品':
                    goodss = pt_good.objects.filter(pk=id)
                else:
                    goodss = query_good('portion', gtype, find='pk', findpara=id)
                if goodss.exists():
                    goodsinfo = list(goodss.values())[0]
                    goods_info = dict(goodsinfo, **order_info[n])
                    good_info_list.append(goods_info)

            goodlist = order_list.objects.filter(order_number=j)

            # 获取拼团商品订单
            if order_goodss.exists():
                ordergoods = order_goodss.filter(userid=userid)
                order = ordergoods.first()

                goodsid = order.goodsid
                # 获取商品
                ptgoods = pt_good.objects.filter(pk=goodsid)
                good_info_list.append(list(ptgoods.values())[0])

            dic3 = {
                'allcount': count,
                'order_info': list(goodlist.values()),
                'goods': good_info_list,
            }
            finally_list.append(dic3)

        data['status'] = '200'
        data['msg'] = 'ok'
        data['content'] = finally_list

    else:
        data['msg'] = '404'
        data['status'] = '用户没有订单'

    return JsonResponse(data)

# 获取拼团商品
def send_pt_goods(request):
    pt_good_list = pt_good.objects.all()
    dic2 = {}
    data = {}

    good_type_list = []
    for info in pt_good_list:
        if info.goodtype not in good_type_list:
            good_type_list.append(info.goodtype)

    dic_list = []
    for n in range(len(good_type_list)):
        dic_list.append(n)
        good_object = pt_good.objects.filter(goodtype=good_type_list[n])
        dic2[good_type_list[n]] = list(good_object.values())

        dic_list[n] = {
            'goodstype': good_type_list[n],
            'goods': dic2[good_type_list[n]],
            'id': n + 1,
        }

    data['stauts'] = '200'
    data['msg'] = 'ok'
    data['content'] = dic_list

    return JsonResponse(data)

# 支付访问接口
def pt_pay(request):
    userid = request.GET.get('userid')
    receive_addr = request.GET.get('receive_addr')
    need_pay_price = request.GET.get('need_pay_price')
    pay_price = request.GET.get('pay_price')
    order_num = request.GET.get('order_num')
    data = {}

    print(userid,receive_addr,need_pay_price,pay_price,order_num)
    orderlist = order_list.objects.filter(order_number=order_num)
    if orderlist.exists():
        order = orderlist.filter(userid=userid).first()
        order.receive_addr = receive_addr
        order.receive_addr = receive_addr
        order.need_pay_price = need_pay_price
        order.pay_price = pay_price

        order.save()

        data['status'] = '200'
        data['msg'] = 'ok'
        data['order_num'] = order_num
        return JsonResponse(data)
    else:
        data['status'] = '404'
        data['msg'] = '订单不存在'

# 生成订单
def create_order(order_num,userid):
    orderlist = order_list()

    orderlist.order_number = order_num
    orderlist.userid = userid
    orderlist.is_pay = 'false'
    orderlist.is_ship = 'false'
    orderlist.is_receipt = 'false'
    orderlist.status = '待付款'
    orderlist.is_pt = 'true'
    timenow = datetime.now().replace(tzinfo=utc)
    orderlist.create_time = timenow

    orderlist.save()

# 开团接口
def start_team(request):
    userid = request.GET.get('userid')
    nickname = request.GET.get('nickname')
    goodid = request.GET.get('goodid')
    data = {}
    print(userid,nickname,goodid)
    user = User.objects.filter(openid=userid).first()
    id = user.id
    import datetime
    timenow = datetime.datetime.now()
    order_num = exchange_time(timenow,id)

    try:
        pt = pt_list()
        pt.userid = userid
        pt.nickname = nickname
        pt.order_number = order_num
        pt.goodsid = goodid
        pt.nowpeople = '1'
        pt.status = '拼团中'

        pt.save()

        create_order(order_num,userid)

        data['status'] = '200'
        data['msg'] = '开团成功'
        data['order_num'] = order_num
        return JsonResponse(data)

    except Exception:
        data['status'] = '300'
        data['msg'] = '出现未知错误'
        return JsonResponse(data)

def pt_order(request):
    order_num = request.GET.get('order_num')
    userid = request.GET.get('userid')
    data = {}

    ptlist = pt_list.objects.filter(order_number=order_num)
    if ptlist.exists():
        ptliss = ptlist.filter(userid=userid)
        try:
            pt = ptliss.first()
            goodsid = pt.goodsid

            market = list(ptliss.values())
            ptgood = pt_good.objects.filter(pk=goodsid)
            # print(ptgood)
            if ptgood.exists():
                goodsinfo = list(ptgood.values())[0]
                goods_info = dict(goodsinfo, **market[0])

                data['status'] = '200'
                data['msg'] = 'ok'
                data['content'] = goods_info

                return JsonResponse(data)
        except Exception:
            data['status'] = '300'
            data['msg'] = '发生异常错误'
            return JsonResponse(data)
    else:
        data['status'] = '404'
        data['msg'] = '订单不存在'

    return JsonResponse(data)

# 加入团
def join_team(request):
    order_num = request.GET.get('order_num')
    userid = request.GET.get('userid')
    nickname = request.GET.get('nickname')
    data = {}

    ptlist = pt_list.objects.filter(order_number=order_num)

    try:
        pt = ptlist.first()
        start_userid = pt.userid
        if start_userid == userid:
            data['status'] = '300'
            data['msg'] = '无法加入自己的拼团'
            return JsonResponse(data)
        # 查询商品最大拼团人数
        pt_goods = pt_good.objects.filter(pk=pt.goodsid)
        ptgood = pt_goods.first()
        most_person = ptgood.pt_people
        nowpeople = pt.nowpeople

        if int(nowpeople) >= int(most_person):
            data['status'] = '300'
            data['msg'] = '拼团人数已满'

            return JsonResponse(data)
        else:
            pt.nowpeople = int(nowpeople) + 1
            pt.save()

            # 加入订单表
            ptlist = pt_list()
            ptlist.userid = userid
            ptlist.nickname = nickname
            ptlist.order_number = order_num
            ptlist.goodsid = pt.goodsid
            ptlist.nowpeople = pt.nowpeople
            ptlist.status = pt.status

            ptlist.save()
            create_order(order_num, userid)

            data['status'] = '200'
            data['msg'] = '拼团成功'
            data['order_num'] = order_num
            return JsonResponse(data)
    except Exception:
        data['status'] = '300'
        data['msg'] = '出现未知错误'
        return JsonResponse(data)

# 获取已开团商品接口
def send_isstart_goods(request):
    goodsid = request.GET.get('goodsid')

    ptlist = pt_list.objects.filter(goodsid=goodsid).filter(status='拼团中')

    goodlist = []
    data = {}

    if ptlist.exists():
        for n in range(len(ptlist)):
            id = ptlist[n].goodsid

            market = list(ptlist.values())

            goodss = pt_good.objects.filter(pk=id)
            if goodss.exists():
                goodsinfo = list(goodss.values())[0]
                goodsinfo['len'] = n
                goods_info = dict(goodsinfo, **market[n])

                goodlist.append(goods_info)

            else:
                data['status'] = '404'
                data['msg'] = '出现未知错误'

        data['status'] = '200'
        data['msg'] = 'ok'
        data['content'] = goodlist
    else:
        data['msg'] = '404'
        data['status'] = '暂无拼团商品'

    return JsonResponse(data)

# 拼团返回订单商品
# def send_order_goods(request):
#     order_num = request.GET.get("order_num")
#
#     data = {}
#     marketlist = []
#
#     market_list = order_list.objects.filter(order_number=order_num)
#
#     if market_list.exists():
#         for n in range(len(market_list)):
#             id = market_list[n].goodsid
#
#             market = list(market_list.values())
#
#             goodss = pt_good.objects.filter(pk=id)
#             if goodss.exists():
#                 goodsinfo = list(goodss.values())[0]
#                 goods_info = dict(goodsinfo, **market[n])
#
#                 marketlist.append(goods_info)
#
#             else:
#                 data['status'] = '404'
#                 data['msg'] = '出现未知错误'
#
#         data['status'] = '200'
#         data['msg'] = 'ok'
#         data['content'] = marketlist
#
#     else:
#         data['status'] = '300'
#         data['msg'] = '未选择任何商品'
#
#     return JsonResponse(data)

# 拼团查看拼团人数,如果满足要求就可开团
def check_person(request):
    order_num = request.GET.get('order_num')
    data = {}

    orderlist = order_goods_list.objects.filter(order_number=order_num)

    try:
        order = orderlist.first()
        goodid = order.goodsid

        goods = pt_good.objects.filter(pk=goodid)
        good = goods.first()
        people_num = good.pt_people
        # 获取现在人数
        ptlist = pt_list.objects.filter(order_number=order_num)
        pt = ptlist.first()
        nowpeople = pt.nowpeople

        if int(people_num) == int(nowpeople):
            data['status'] = '200'
            data['msg'] = '人数已满,可以开启拼团'
        elif int(people_num) > int(nowpeople):
            data['status'] = '300'
            data['msg'] = '人数不足,无法开启拼团'

        return JsonResponse(data)
    except Exception:
        data['status'] = '300'
        data['msg'] = '发生异常错误'

        return JsonResponse(data)

# 查看拼团商品是否过期
def check_isdate(request):
    goodid = request.GET.get('goodid')
    data = {}

    ptlist = pt_good.objects.filter(pk=goodid)
    try:
        good = ptlist.first()
        pt_end_time = good.pt_end_time

        timenow = datetime.now().replace(tzinfo=utc)

        result = int(time.mktime(timenow.timetuple())) - int(time.mktime(pt_end_time.timetuple()))
        if result >= 0:
            data['status'] = '300'
            data['msg'] = '此拼团商品已过期'
            good.status = '已过期'

            good.save()

        else:
            data['status'] = '200'
            data['msg'] = '拼团商品未过期'

        return JsonResponse(data)
    except Exception:
        data['status'] = '300'
        data['msg'] = '发生异常错误'

        return JsonResponse(data)

# 取消订单
def cancel_order(request):
    order_num = request.GET.get('order_num')

    orderlist = order_list.objects.filter(order_number=order_num)
    if orderlist.exists():
        for order in orderlist:
            order.delete()
    else:
        data = {
            'status': '404',
            'msg': '订单不存在'
        }
        return JsonResponse(data)

    orderss = order_goods_list.objects.filter(order_number=order_num)
    if orderss.exists():
        for order in orderss:
            order.delete()

    else:
        data = {
            'status': '300',
            'msg': '该订单为拼团订单,无法取消'
        }
        return JsonResponse(data)

    data = {
        'status': '200',
        'msg': '订单取消成功'
    }

    return JsonResponse(data)

# 查询订单
def query_order(request):
    order_num = request.GET.get('order_num')
    data = {}

    orderlist = order_list.objects.filter(order_number=order_num)
    if orderlist.exists():
        data['status'] = '200'
        data['msg'] = 'ok'
        data['content'] = list(orderlist.values())
        data['order_num'] = order_num
    else:
        data['status'] = '404'
        data['msg'] = '订单不存在'

    return JsonResponse(data)

# 开团
def open_team(request):
    order_num = request.GET.get('order_num')
    data ={}

    ptlist = pt_list.objects.filter(order_number=order_num)
    orderlist = order_list.objects.filter(order_number=order_num)
    try:
        for pt in ptlist:
            pt.status = '已开团'
            pt.save()

        order = orderlist.first()
        order.is_complish = 'true'
        order.save()

        data['status'] = '200'
        data['msg'] = 'ok'
        return JsonResponse(data)
    except Exception:
        data['status'] = '300'
        data['msg'] = '出现异常错误'

# 清除未付款的团
def delete_team(request):
    goodsid = request.GET.get('goodsid')
    data = {}
    order_num_list = []
    order_num_list1 = []

    ptlist = pt_list.objects.filter(goodsid=goodsid)
    if ptlist.exists():
        for pt in ptlist:
            if pt.order_number not in order_num_list:
                order_num_list.append(pt.order_number)
        print(order_num_list)
        for order_num in order_num_list:
            orderlist = order_list.objects.filter(order_number=order_num)
            if orderlist.exists():
                for order in orderlist:
                    print(order.status)
                    if order.status == '待付款':
                        print('删除页面')
                        order_num_list1.append(order.order_number)
                        order.delete()

        for order_num in order_num_list1:
            ptlists = pt_list.objects.filter(order_number=order_num)
            if ptlists.exists():
                for pt in ptlists:
                    pt.delete()

        data['status'] = '200'
        data['msg'] = '清除完成'

    else:
        data['status'] = '201'
        data['msg'] = '没有已开的团'

    return JsonResponse(data)



























































































