from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from mlsx.models import food_goods, nofood_goods, fresh_goods, out_window_goods, fruit_goods, vegetable_goods, \
    dry_fruit_goods, meat_goods

def first_classify(request):
    data = {
        'status': '200',
        'msg': 'ok'
    }

    data['content'] = [{'type':'粮油副食'},{'type':'日常百货'},{'type':'精选生鲜'},{'type':'外场窗口'},
                       {'type':'新鲜水果'},{'type':'净菜蔬菜'},{'type':'坚果干货'},{'type':'肉禽蛋类'}]

    return JsonResponse(data)

def query_good(findtype,goods_type,findpara=None):
    goods_list = []
    if findtype == 'all':
        if goods_type == '粮油副食':
            goods_list = food_goods.objects.all()
        if goods_type == '日常百货':
            goods_list = nofood_goods.objects.all()
        if goods_type == '精选生鲜':
            goods_list = fresh_goods.objects.all()
        if goods_type == '外场窗口':
            goods_list = out_window_goods.objects.all()
        if goods_type == '新鲜水果':
            goods_list = fruit_goods.objects.all()
        if goods_type == '净菜蔬菜':
            goods_list = vegetable_goods.objects.all()
        if goods_type == '坚果干货':
            goods_list = dry_fruit_goods.objects.all()
        if goods_type == '肉禽蛋类':
            goods_list = meat_goods.objects.all()

        return goods_list

    elif findtype == 'portion':
        pass

def send_goods(request):
    data = {
        'status': '200',
        'msg': 'ok'
    }

    # 获取从前端传回的商品类型
    goods_type = request.GET.get('type')

    if goods_type == '粮油副食':
        goods_list = food_goods.objects.all()
    if goods_type == '日常百货':
        goods_list = nofood_goods.objects.all()
    if goods_type == '精选生鲜':
        goods_list = fresh_goods.objects.all()
    if goods_type == '外场窗口':
        goods_list = out_window_goods.objects.all()
    if goods_type == '新鲜水果':
        goods_list = fruit_goods.objects.all()
    if goods_type == '净菜蔬菜':
        goods_list = vegetable_goods.objects.all()
    if goods_type == '坚果干货':
        goods_list = dry_fruit_goods.objects.all()
    if goods_type == '肉禽蛋类':
        goods_list = meat_goods.objects.all()

    good_type_list = []
    for info in goods_list:
        if info.goodsType not in good_type_list:
            good_type_list.append(info.goodsType)

    for goodtype in good_type_list:
        good_object = fruit_goods.objects.filter(goodsType=goodtype)
        data[goodtype] = list(good_object.values())

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

def findbyname(request):
    goodsname = request.GET.get('goodsname')
    data = {}

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

    if not goods_list.exists():
        data['status'] = '404'
        data['msg'] = '不存在此商品'

    else:
        data['status'] = '200'
        data['msg'] = 'ok'
        data['content'] = list(goods_list.first().values())

    return JsonResponse(data)

# 将商品添入购物车的接口
def addcart(request):
    goodid = request.GET.get('goodid')

    # 根据商品编号查找商品













































































