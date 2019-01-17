import time
from datetime import datetime
from pprint import pprint

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.timezone import utc

from mlsx.models import food_goods, nofood_goods, fresh_goods, out_window_goods, fruit_goods, vegetable_goods, \
    dry_fruit_goods, meat_goods, Market, User, vip, morning_market


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
    print(info)

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

    # 根据商品编号查找商品
    goodlist = query_good('portion',goods_type,find='pk',findpara=goodid)
    # print(goodid,goods_type,userid)
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
                market.goods_price = good.retail_price
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
    # print(goods_list)
    # print(len(goods_list),'len')
    if goods_list.exists():
        for n in range(len(goods_list)):
            id = goods_list[n].goodsid
            gtype = goods_list[n].goodstype

            market = list(goods_list.values())

            goodss = query_good('portion',gtype,find='pk',findpara=id)
            if goodss.exists():
                goodsinfo = list(goodss.values())[0]
                goods_info = dict(goodsinfo,**market[n])

                goodlist.append(goods_info)

            else:
                data['status'] = '404'
                data['msg'] = '出现未知错误'

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

    market = Market.objects.filter(userid=userid).filter(goodid=goodid)

    if market.exists():
        # 获取当前加入购物车的数量
        count = int(market.buycount)
        market.buycount = str(count + 1)
        data['status'] = '200'
        data['msg'] = 'ok'

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

    market = Market.objects.filter(userid=userid).filter(goodid=goodid)

    # 获取当前加入购物车的数量
    count = market.buycount
    if count == '1':
        market.delete()
        market.save()
        data['status'] = '201'
        data['msg'] = '商品已从购物车删除'

    else:
        market.buycount = count - 1
        market.save()

        data['status'] = '200'
        data['msg'] = 'ok'

    return JsonResponse(data)

# 根据条件排序
def sort_goods(request):
    sort_type = request.GET.get('sort_type')
    goodstype = request.GET.get('type')
    goodstype2 = request.GET.get('type2')

    data = {}
    goodslist = []

    if sort_type == '综合':
        goodslist = query_good('all',goodstype)
        data['content'] = list(goodslist.value())

    elif sort_type == '最新':
        pass

    elif sort_type == '价格顺序':
        goodslist = query_good('portion',goodslist,find='goodsType',findpara=goodstype2).order_by('retail_price')
        data['content'] = list(goodslist.value())

    elif sort_type == '价格逆序':
        goodslist = query_good('portion', goodslist, find='goodsType', findpara=goodstype2).order_by('-retail_price')
        data['content'] = list(goodslist.value())

    elif sort_type == '销量':
        pass

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
    # 从数据库中查询vip天数
    viplist = vip.objects.filter(viptime=time)

    if viplist.exists():
        vips = viplist.first()
        vipdays = vips.days
        viptypes = vip.viptype

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
        users.vip_end_time = timenow + datetime.timedelta(days=vipdays)
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
        users.vip_end_time = timenow + datetime.timedelta(days=vipdays)
        # 获取最后一个用户id并加一
        userss = User.objects.all()
        finuser = userss.last()

        users.vipid = finuser.id
        users.userType = viptypes

        users.save()
        data['status'] = '200'
        data['msg'] = '添加并开通成功'

    return JsonResponse(data)

# 查询会员对应规则
def query_vip(request):
    viplist = vip.objects.all()
    data = {}
    vip_list = []

    vip_type_list = []
    for info in viplist:
        if info.goodsType not in vip_type_list:
            vip_type_list.append(info.viptype)

    for vip_type in vip_type_list:
        vip_object = vip.objects.filter(viptype=1)
        viplist.append({
            'type': vip_type,
            'content': list(vip_object.values())
        })

    data['status'] = '200'
    data['msg'] = 'ok'
    data['content'] = vip_list

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

    if goodlist.length >= int(count):
        goods = goodlist[0:int(count)]
        data['stauts'] = '200'
        data['msg'] = 'ok'
        data['content'] = list(goods.values())

    else:
        data['stauts'] = '300'
        data['msg'] = '没有这么多商品'

    return JsonResponse(data)

# 订单接口
def order(request):
    userid = request.GET.get("userid")
    # 获取前端计算出来的总价
    total_price = request.GET.get('total_price')
    data = {}

    # 从购物车中找出已选中的商品
    market_list = Market.objects.filter(userid=userid).filter(isselect='true')
    if market_list.exists():
        pass

    else:
        data['status'] = '300'
        data['msg'] = '未选择任何商品'

# 购物车商品选中,取消接口
def goods_select(request):
    select = request.GET.get('select')
    goodid = request.GET.get('id')
    data = {}

    marketlist = Market.objects.filter(goodsid=goodid)

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








































































































