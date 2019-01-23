from django.db import models

# Create your models here.
class User(models.Model):
    openid = models.TextField()
    nickname = models.TextField(null=True)
    userType = models.TextField(default='普通会员')
    vipid = models.TextField(null=True)
    enquiry = models.TextField(default=0)
    vip_start_time = models.DateTimeField(null=True)
    vip_end_time = models.DateTimeField(null=True)
    phone_num = models.TextField(null=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'

class food_goods(models.Model):
    bar_code = models.TextField(null=True)
    coding = models.TextField(null=True)
    maingoods_coding = models.TextField(null=True)
    goodsname = models.TextField(null=True)
    unit = models.TextField(null=True)
    package = models.TextField(null=True)
    goodsType = models.TextField(null=True)
    goods_classify_code = models.TextField(null=True)
    supplier = models.TextField(null=True)
    expiration_date = models.TextField(null=True)
    origin = models.TextField(null=True)
    count_type = models.TextField(null=True)
    goodsStatus = models.TextField(null=True)
    cost = models.TextField(null=True)
    retail_price = models.TextField(null=True)
    vip_price = models.TextField(null=True)
    send_price = models.TextField(null=True)
    trade_price = models.TextField(null=True)
    minimum_stock = models.TextField(null=True)
    highest_stock = models.TextField(null=True)
    initial_amount = models.TextField(null=True)
    initial_count = models.TextField(null=True)
    replenishment_logo = models.TextField(null=True)
    replenishment_period = models.TextField(null=True)
    minimum_replenishment_volume = models.TextField(null=True)
    standard = models.TextField(null=True)
    goodsMode = models.TextField(null=True)
    brand = models.TextField(null=True)
    remark = models.TextField(null=True)
    goods_img = models.ImageField(upload_to='goods_img',null=True)
    goods_desc = models.TextField(null=True)
    goods_detail_img1 = models.ImageField(upload_to='goods_detail_img1',null=True)
    goods_detail_img2 = models.ImageField(upload_to='goods_detail_img2', null=True)
    storage = models.TextField(null=True)
    sales = models.TextField(null=True)

    class Meta:
        db_table = 'food_goods'

class nofood_goods(models.Model):
    bar_code = models.TextField(null=True)
    coding = models.TextField(null=True)
    maingoods_coding = models.TextField(null=True)
    goodsname = models.TextField(null=True)
    unit = models.TextField(null=True)
    package = models.TextField(null=True)
    goodsType = models.TextField(null=True)
    goods_classify_code = models.TextField(null=True)
    supplier = models.TextField(null=True)
    expiration_date = models.TextField(null=True)
    origin = models.TextField(null=True)
    count_type = models.TextField(null=True)
    goodsStatus = models.TextField(null=True)
    cost = models.TextField(null=True)
    retail_price = models.TextField(null=True)
    vip_price = models.TextField(null=True)
    send_price = models.TextField(null=True)
    trade_price = models.TextField(null=True)
    minimum_stock = models.TextField(null=True)
    highest_stock = models.TextField(null=True)
    initial_amount = models.TextField(null=True)
    initial_count = models.TextField(null=True)
    replenishment_logo = models.TextField(null=True)
    replenishment_period = models.TextField(null=True)
    minimum_replenishment_volume = models.TextField(null=True)
    standard = models.TextField(null=True)
    goodsMode = models.TextField(null=True)
    brand = models.TextField(null=True)
    remark = models.TextField(null=True)
    goods_img = models.ImageField(upload_to='goods_img',null=True)
    goods_desc = models.TextField(null=True)
    goods_detail_img1 = models.ImageField(upload_to='goods_detail_img1',null=True)
    goods_detail_img2 = models.ImageField(upload_to='goods_detail_img2', null=True)
    storage = models.TextField(null=True)
    sales = models.TextField(null=True)

    class Meta:
        db_table = 'nofood_goods'

class fresh_goods(models.Model):
    bar_code = models.TextField(null=True)
    coding = models.TextField(null=True)
    maingoods_coding = models.TextField(null=True)
    goodsname = models.TextField(null=True)
    unit = models.TextField(null=True)
    package = models.TextField(null=True)
    goodsType = models.TextField(null=True)
    goods_classify_code = models.TextField(null=True)
    supplier = models.TextField(null=True)
    expiration_date = models.TextField(null=True)
    origin = models.TextField(null=True)
    count_type = models.TextField(null=True)
    goodsStatus = models.TextField(null=True)
    cost = models.TextField(null=True)
    retail_price = models.TextField(null=True)
    vip_price = models.TextField(null=True)
    send_price = models.TextField(null=True)
    trade_price = models.TextField(null=True)
    minimum_stock = models.TextField(null=True)
    highest_stock = models.TextField(null=True)
    initial_amount = models.TextField(null=True)
    initial_count = models.TextField(null=True)
    replenishment_logo = models.TextField(null=True)
    replenishment_period = models.TextField(null=True)
    minimum_replenishment_volume = models.TextField(null=True)
    standard = models.TextField(null=True)
    goodsMode = models.TextField(null=True)
    brand = models.TextField(null=True)
    remark = models.TextField(null=True)
    goods_img = models.ImageField(upload_to='goods_img',null=True)
    goods_desc = models.TextField(null=True)
    goods_detail_img1 = models.ImageField(upload_to='goods_detail_img1',null=True)
    goods_detail_img2 = models.ImageField(upload_to='goods_detail_img2', null=True)
    storage = models.TextField(null=True)
    sales = models.TextField(null=True)

    class Meta:
        db_table = 'fresh_goods'

class out_window_goods(models.Model):
    bar_code = models.TextField(null=True)
    coding = models.TextField(null=True)
    maingoods_coding = models.TextField(null=True)
    goodsname = models.TextField(null=True)
    unit = models.TextField(null=True)
    package = models.TextField(null=True)
    goodsType = models.TextField(null=True)
    goods_classify_code = models.TextField(null=True)
    supplier = models.TextField(null=True)
    expiration_date = models.TextField(null=True)
    origin = models.TextField(null=True)
    count_type = models.TextField(null=True)
    goodsStatus = models.TextField(null=True)
    cost = models.TextField(null=True)
    retail_price = models.TextField(null=True)
    vip_price = models.TextField(null=True)
    send_price = models.TextField(null=True)
    trade_price = models.TextField(null=True)
    minimum_stock = models.TextField(null=True)
    highest_stock = models.TextField(null=True)
    initial_amount = models.TextField(null=True)
    initial_count = models.TextField(null=True)
    replenishment_logo = models.TextField(null=True)
    replenishment_period = models.TextField(null=True)
    minimum_replenishment_volume = models.TextField(null=True)
    standard = models.TextField(null=True)
    goodsMode = models.TextField(null=True)
    brand = models.TextField(null=True)
    remark = models.TextField(null=True)
    goods_img = models.ImageField(upload_to='goods_img',null=True)
    goods_desc = models.TextField(null=True)
    goods_detail_img1 = models.ImageField(upload_to='goods_detail_img1',null=True)
    goods_detail_img2 = models.ImageField(upload_to='goods_detail_img2', null=True)
    storage = models.TextField(null=True)
    sales = models.TextField(null=True)

    class Meta:
        db_table = 'out_window_goods'

class fruit_goods(models.Model):
    bar_code = models.TextField(null=True)
    coding = models.TextField(null=True)
    maingoods_coding = models.TextField(null=True)
    goodsname = models.TextField(null=True)
    unit = models.TextField(null=True)
    package = models.TextField(null=True)
    goodsType = models.TextField(null=True)
    goods_classify_code = models.TextField(null=True)
    supplier = models.TextField(null=True)
    expiration_date = models.TextField(null=True)
    origin = models.TextField(null=True)
    count_type = models.TextField(null=True)
    goodsStatus = models.TextField(null=True)
    cost = models.TextField(null=True)
    retail_price = models.TextField(null=True)
    vip_price = models.TextField(null=True)
    send_price = models.TextField(null=True)
    trade_price = models.TextField(null=True)
    minimum_stock = models.TextField(null=True)
    highest_stock = models.TextField(null=True)
    initial_amount = models.TextField(null=True)
    initial_count = models.TextField(null=True)
    replenishment_logo = models.TextField(null=True)
    replenishment_period = models.TextField(null=True)
    minimum_replenishment_volume = models.TextField(null=True)
    standard = models.TextField(null=True)
    goodsMode = models.TextField(null=True)
    brand = models.TextField(null=True)
    remark = models.TextField(null=True)
    goods_img = models.ImageField(upload_to='goods_img',null=True)
    goods_desc = models.TextField(null=True)
    goods_detail_img1 = models.ImageField(upload_to='goods_detail_img1',null=True)
    goods_detail_img2 = models.ImageField(upload_to='goods_detail_img2', null=True)
    storage = models.TextField(null=True)
    sales = models.TextField(null=True)

    class Meta:
        db_table = 'fruit_goods'

class vegetable_goods(models.Model):
    bar_code = models.TextField(null=True)
    coding = models.TextField(null=True)
    maingoods_coding = models.TextField(null=True)
    goodsname = models.TextField(null=True)
    unit = models.TextField(null=True)
    package = models.TextField(null=True)
    goodsType = models.TextField(null=True)
    goods_classify_code = models.TextField(null=True)
    supplier = models.TextField(null=True)
    expiration_date = models.TextField(null=True)
    origin = models.TextField(null=True)
    count_type = models.TextField(null=True)
    goodsStatus = models.TextField(null=True)
    cost = models.TextField(null=True)
    retail_price = models.TextField(null=True)
    vip_price = models.TextField(null=True)
    send_price = models.TextField(null=True)
    trade_price = models.TextField(null=True)
    minimum_stock = models.TextField(null=True)
    highest_stock = models.TextField(null=True)
    initial_amount = models.TextField(null=True)
    initial_count = models.TextField(null=True)
    replenishment_logo = models.TextField(null=True)
    replenishment_period = models.TextField(null=True)
    minimum_replenishment_volume = models.TextField(null=True)
    standard = models.TextField(null=True)
    goodsMode = models.TextField(null=True)
    brand = models.TextField(null=True)
    remark = models.TextField(null=True)
    goods_img = models.ImageField(upload_to='goods_img',null=True)
    goods_desc = models.TextField(null=True)
    goods_detail_img1 = models.ImageField(upload_to='goods_detail_img1',null=True)
    goods_detail_img2 = models.ImageField(upload_to='goods_detail_img2', null=True)
    storage = models.TextField(null=True)
    sales = models.TextField(null=True)

    class Meta:
        db_table = 'vegetable_goods'

class dry_fruit_goods(models.Model):
    bar_code = models.TextField(null=True)
    coding = models.TextField(null=True)
    maingoods_coding = models.TextField(null=True)
    goodsname = models.TextField(null=True)
    unit = models.TextField(null=True)
    package = models.TextField(null=True)
    goodsType = models.TextField(null=True)
    goods_classify_code = models.TextField(null=True)
    supplier = models.TextField(null=True)
    expiration_date = models.TextField(null=True)
    origin = models.TextField(null=True)
    count_type = models.TextField(null=True)
    goodsStatus = models.TextField(null=True)
    cost = models.TextField(null=True)
    retail_price = models.TextField(null=True)
    vip_price = models.TextField(null=True)
    send_price = models.TextField(null=True)
    trade_price = models.TextField(null=True)
    minimum_stock = models.TextField(null=True)
    highest_stock = models.TextField(null=True)
    initial_amount = models.TextField(null=True)
    initial_count = models.TextField(null=True)
    replenishment_logo = models.TextField(null=True)
    replenishment_period = models.TextField(null=True)
    minimum_replenishment_volume = models.TextField(null=True)
    standard = models.TextField(null=True)
    goodsMode = models.TextField(null=True)
    brand = models.TextField(null=True)
    remark = models.TextField(null=True)
    goods_img = models.ImageField(upload_to='goods_img',null=True)
    goods_desc = models.TextField(null=True)
    goods_detail_img1 = models.ImageField(upload_to='goods_detail_img1',null=True)
    goods_detail_img2 = models.ImageField(upload_to='goods_detail_img2', null=True)
    storage = models.TextField(null=True)
    sales = models.TextField(null=True)

    class Meta:
        db_table = 'dry_fruit_goods'

class meat_goods(models.Model):
    bar_code = models.TextField(null=True)
    coding = models.TextField(null=True)
    maingoods_coding = models.TextField(null=True)
    goodsname = models.TextField(null=True)
    unit = models.TextField(null=True)
    package = models.TextField(null=True)
    goodsType = models.TextField(null=True)
    goods_classify_code = models.TextField(null=True)
    supplier = models.TextField(null=True)
    expiration_date = models.TextField(null=True)
    origin = models.TextField(null=True)
    count_type = models.TextField(null=True)
    goodsStatus = models.TextField(null=True)
    cost = models.TextField(null=True)
    retail_price = models.TextField(null=True)
    vip_price = models.TextField(null=True)
    send_price = models.TextField(null=True)
    trade_price = models.TextField(null=True)
    minimum_stock = models.TextField(null=True)
    highest_stock = models.TextField(null=True)
    initial_amount = models.TextField(null=True)
    initial_count = models.TextField(null=True)
    replenishment_logo = models.TextField(null=True)
    replenishment_period = models.TextField(null=True)
    minimum_replenishment_volume = models.TextField(null=True)
    standard = models.TextField(null=True)
    goodsMode = models.TextField(null=True)
    brand = models.TextField(null=True)
    remark = models.TextField(null=True)
    goods_img = models.ImageField(upload_to='goods_img',null=True)
    goods_desc = models.TextField(null=True)
    goods_detail_img1 = models.ImageField(upload_to='goods_detail_img1',null=True)
    goods_detail_img2 = models.ImageField(upload_to='goods_detail_img2', null=True)
    storage = models.TextField(null=True)
    sales = models.TextField(null=True)

    class Meta:
        db_table = 'meat_goods'


class Market(models.Model):
    userid = models.TextField()
    goodsid = models.TextField()
    buycount = models.TextField()
    goods_price = models.TextField()
    goods_vip_price = models.TextField()
    isselect = models.TextField()
    is_morning = models.TextField()
    goodstype = models.TextField()

    class Meta:
        db_table = 'market'

# 拼团商品表
class pt_good(models.Model):
    goodname = models.TextField()
    unit = models.TextField()
    goodtype = models.TextField()
    pt_price = models.TextField()
    price = models.TextField()
    standard = models.TextField()
    goods_img = models.ImageField(upload_to='img',null=True)
    goods_img1 = models.ImageField(upload_to='img',null=True)
    pt_start_time = models.DateTimeField()
    pt_end_time = models.DateTimeField()
    update_time = models.DateTimeField(auto_now=True,null=True)
    storage = models.TextField()
    pt_people = models.TextField()

    class Meta:
        db_table = 'pt_good'

# 拼团列表
class pt_list(models.Model):
    userid = models.TextField()
    nickname = models.TextField(null=True)
    order_number = models.TextField()
    goodsid = models.TextField()
    nowpeople = models.TextField()
    status = models.TextField()

    class Meta:
        db_table = 'pt_list'

class vip(models.Model):
    viptime = models.TextField()
    price = models.TextField()
    days = models.TextField()
    viptype = models.TextField()

    class Meta:
        db_table = 'vip'

# 订单表
class order_list(models.Model):
    order_number = models.CharField(max_length=128)
    userid = models.TextField()
    need_pay_price = models.TextField(null=True)
    pay_price = models.TextField(null=True)
    is_pay = models.TextField()
    pay_time = models.DateTimeField(null=True)
    is_ship = models.TextField()
    ship_time = models.DateTimeField(null=True)
    is_receipt = models.TextField()
    receipt_time = models.TextField(null=True)
    status = models.TextField()
    receive_addr = models.TextField()
    remark = models.TextField(null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(auto_now=True)
    is_pt = models.TextField(default='false')
    is_complish = models.TextField(default='false')

    class Meta:
        db_table = 'order_list'

# 订单商品表
class order_goods_list (models.Model):
    order_number = models.CharField(max_length=128)
    goodsid = models.TextField()
    goodstype = models.TextField()
    userid = models.TextField()
    goods_num = models.TextField()
    goodsprice = models.TextField()
    is_estimate = models.TextField(default='false')
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'order_goods_list'

# 早市表
class morning_market(models.Model):
    goodname = models.TextField()
    unit = models.TextField()
    goodtype = models.TextField()
    promotion_price = models.TextField()
    price = models.TextField()
    standard = models.TextField()
    goods_img = models.ImageField(upload_to='zaoshi',null=True)
    goods_img1 = models.ImageField(upload_to='zaoshi',null=True)
    storage = models.TextField()
    zx_start_time = models.DateTimeField()
    zx_end_time = models.DateTimeField()
    update_time = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        db_table = 'morning_market'

# 商品评价表
class goods_estimate(models.Model):
    order_number = models.TextField()
    userid = models.TextField()
    estimate_type = models.TextField()
    goods_descripe = models.TextField(null=True)
    send_server = models.TextField(null=True)
    server_attitute = models.TextField(null=True)

    class Meta:
        db_table = 'goods_estimate'

























