from django.db import models

# Create your models here.
class User(models.Model):
    openid = models.TextField()
    userType = models.TextField(default='普通会员')
    vipid = models.TextField(null=True)
    enquiry = models.TextField(default=0)
    vip_start_time = models.DateTimeField(null=True,auto_now_add=True)
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

class pintuan(models.Model):
    goodid = models.TextField()
    userid = models.TextField()
    pintuan_code = models.TextField()

    class Meta:
        db_table = 'pintuan'

# 拼团表
class pt_good(models.Model):
    goodname = models.TextField()
    unit = models.TextField()
    goodtype = models.TextField()
    pt_price = models.TextField()
    price = models.TextField()
    standard = models.TextField()
    pt_start_time = models.DateTimeField(auto_now_add=True)
    pt_end_time = models.DateTimeField()
    update_time = models.DateTimeField(auto_now=True)
    pt_people = models.TextField()

    class Meta:
        db_table = 'pt_good'

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
    pay_price = models.TextField()
    is_pay = models.TextField()
    pay_time = models.DateTimeField()
    is_ship = models.TextField()
    ship_time = models.DateTimeField()
    is_receipt = models.TextField()
    receipt_time = models.TextField()
    status = models.TextField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        db_table = 'order_list'

# 订单商品表
class order_goods_list (models.Model):
    order_number = models.CharField(max_length=128)
    goodsid = models.TextField()
    userid = models.TextField()
    goods_num = models.TextField()
    goodsprice = models.TextField()
    status = models.TextField()
    create_time = models.TextField()
    update_time = models.TextField()
    pay_time = models.TextField()

# 早市表
class morning_market(models.Model):
    goodname = models.TextField()
    unit = models.TextField()
    goodtype = models.TextField()
    promotion_price = models.TextField()
    price = models.TextField()
    standard = models.TextField()
    pt_start_time = models.DateTimeField(auto_now_add=True)
    pt_end_time = models.DateTimeField()
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'morning_market'



