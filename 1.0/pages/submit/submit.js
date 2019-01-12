// pages/cart/cart.js
Page({


  data: {
    isAllSelect: false,
    totalMoney: 0,
    num: 0,
    cart_id: 1,
    paymoney: 0,
    sendmoney: 3,
    // 商品详情介绍
    carts: [{
      id: 1,
      is_buy: 1,
      buynum: 1,
      minusStatus: 'disabled',
      pic: "http://59.110.218.60/images/cart_page/submit/3.png",
      name: "新鲜的大白菜",
      introduce: '绿色健康，富含活力花青素',
      weight: '600g',
      price: 3,
      isSelect: false,
    },
    {
      id: 2,
      is_buy: 1,
      buynum: 1,
      minusStatus: 'disabled',
      pic: "http://59.110.218.60/images/cart_page/submit/3.png",
      name: "新鲜的大白菜",
      introduce: '绿色健康，富含活力花青素',
      weight: '600g',
      price: 3,
      isSelect: false,
    },
    {
      id: 3,
      is_buy: 1,
      buynum: 1,
      minusStatus: 'disabled',
      pic: "http://59.110.218.60/images/cart_page/submit/3.png",
      name: "新鲜的大白菜",
      introduce: '绿色健康，富含活力花青素',
      weight: '600g',
      price: 3,
      isSelect: false,
    },
    {
      id: 4,
      is_buy: 1,
      buynum: 1,
      minusStatus: 'disabled',
      pic: "http://59.110.218.60/images/cart_page/submit/3.png",
      name: "新鲜的大白菜",
      introduce: '绿色健康，富含活力花青素',
      weight: '600g',
      price: 3,
      isSelect: false,
    },
    ],
    curNav: 1,
    goods: 4,
    // curIndex: 0
  },

  onShow: function(options) {
    // console.log('页面加载')
    // var goods = this.data.goods
    // console.log(goods)
    // if (goods <= 0) {
    //   wx.navigateTo({
    //     url: '/pages/emptycart/emptycart',
    //     success: function(res) {},
    //     fail: function(res) {},
    //     complete: function(res) {},
    //   })
    // } else {

    // }
  },

  //勾选事件处理函数  
  switchSelect: function (e) {
    // 获取item项的id，和数组的下标值  
    var Allprice = 0,
      i = 0;
    let id = e.target.dataset.id,

      index = parseInt(e.target.dataset.index);
    this.data.carts[index].isSelect = !this.data.carts[index].isSelect;
    //价钱统计
    if (this.data.carts[index].isSelect) {
      this.data.totalMoney = this.data.totalMoney + this.data.carts[index].price * this.data.carts[index].buynum;
    } else {
      this.data.totalMoney = this.data.totalMoney - this.data.carts[index].price * this.data.carts[index].buynum;
    }


    //是否全选判断
    for (i = 0; i < this.data.carts.length; i++) {
      Allprice = Allprice + this.data.carts[i].price;
    }
    if (Allprice == this.data.totalMoney) {
      this.data.isAllSelect = true;
    } else {
      this.data.isAllSelect = false;
    }
    this.setData({
      carts: this.data.carts,
      totalMoney: this.data.totalMoney,
      isAllSelect: this.data.isAllSelect,
    })
  },
  //全选
  allSelect: function (e) {
    //处理全选逻辑
    let i = 0;
    this.data.totalMoney = 0
    var paymoney = this.data.paymoney
    var sendmoney = this.data.sendmoney
    paymoney = 0

    if (!this.data.isAllSelect) {
      for (i = 0; i < this.data.carts.length; i++) {
        this.data.carts[i].isSelect = true;
        if (this.data.carts[i].is_buy == 1) {
          this.data.totalMoney = this.data.totalMoney + this.data.carts[i].price * this.data.carts[i].buynum;
        }
      }
    } else {
      for (i = 0; i < this.data.carts.length; i++) {
        this.data.carts[i].isSelect = false;
      }
      this.data.totalMoney = 0;
    }
    this.setData({
      carts: this.data.carts,
      isAllSelect: !this.data.isAllSelect,
      totalMoney: this.data.totalMoney,
      paymoney: paymoney + sendmoney + this.data.totalMoney,
    })
  },
  // 去结算
  toBuy() {
    wx.showToast({
      title: '去结算',
      icon: 'success',
      duration: 3000
    });

    this.setData({
      showDialog: !this.data.showDialog
    });
  },
  //数量变化处理
  handleQuantityChange(e) {
    var componentId = e.componentId;
    var quantity = e.quantity;
    this.data.carts[componentId].count.quantity = quantity;
    this.setData({
      carts: this.data.carts,
    });
  },

  subgoods: function (t) {
    // var type = this.data.curIndex
    var goodid = t.currentTarget.dataset.id
    var ids = parseInt(goodid) - 1
    var buynum = this.data.carts[ids].buynum
    var e = this
    var goods = this.data.goods
    var totalMoney = this.data.totalMoney
    var price = this.data.carts[ids].price
    var paymoney = this.data.paymoney
    var sendmoney = this.data.sendmoney
    // console.log(typeof(buynum))
    // console.log(goods)

    if (buynum == 1) {
      // console.log(111)
      wx.showModal({
        title: '您确定删除该商品吗?',
        // content: '模态弹窗',
        success: function (res) {
          if (res.confirm) {
            var sItem = "carts[" + ids + "].is_buy";
            e.setData({
              [sItem]: 0,
              goods: goods - 1,
              
            })
            if (e.data.carts[ids].isSelect == true) {
              e.setData({
                totalMoney: totalMoney - price,
                paymoney: paymoney - price
              })
            }
            
            // if (goods <= 1) {
            //   wx.navigateTo({
            //     url: '/pages/emptycart/emptycart',
            //     success: function (res) { },
            //     fail: function (res) { },
            //     complete: function (res) { },
            //   })
            // }
          } else {
            console.log('用户点击取消')
          }
        }
      })
    } else {
      var buynums = "carts[" + ids + "].buynum";

      e.setData({
        [buynums]: buynum - 1,
      })
      if (e.data.carts[ids].isSelect == true) {
        e.setData({
          totalMoney: totalMoney - price,
          paymoney: paymoney - price
        })
      }
    }

  },

  addgoods: function (t) {
    // var type = this.data.curIndex
    var goodid = t.currentTarget.dataset.id
    var ids = parseInt(goodid) - 1
    var buynum = this.data.carts[ids].buynum
    var buynums = "carts[" + ids + "].buynum";
    var totalMoney = this.data.totalMoney
    var paymoney = this.data.paymoney
    var sendmoney = this.data.sendmoney
    paymoney = 0

    if (this.data.carts[ids].isSelect == true) {
      this.setData({
        totalMoney: totalMoney + this.data.carts[ids].price
      })
    }

    this.setData({
      [buynums]: buynum + 1,
      paymoney: paymoney + sendmoney + this.data.totalMoney,
    })
    // }  
  },

})