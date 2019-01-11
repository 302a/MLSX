// pages/cart/cart.js
Page({


  data: {
    isAllSelect: false,
    totalMoney: 0,
    num:0,
    cart_id:1,
    // 商品详情介绍
    carts: [
      {
        id:1,
        is_buy: 0,
        buynum: 1,
        minusStatus:'disabled',
        pic: "http://59.110.218.60/cart_page/submit/3.png",
        name: "新鲜的大白菜",
        introduce: '绿色健康，富含活力花青素',
        weight:'600g',
        price: 3,
        isSelect: false,
            },
      {
        id: 2,
        is_buy: 0,
        buynum: 1,
        minusStatus: 'disabled',
        pic: "http://59.110.218.60/cart_page/submit/3.png",
        name: "新鲜的大白菜",
        introduce: '绿色健康，富含活力花青素',
        weight: '600g',
        price: 3,
        isSelect: false,
      },
      {
        id: 3,
        is_buy: 0,
        buynum: 1,
        minusStatus: 'disabled',
        pic: "http://59.110.218.60/cart_page/submit/3.png",
        name: "新鲜的大白菜",
        introduce: '绿色健康，富含活力花青素',
        weight: '600g',
        price: 3,
        isSelect: false,
      },
      {
        id: 4,
        is_buy: 0,
        buynum: 1,
        minusStatus: 'disabled',
        pic: "http://59.110.218.60/cart_page/submit/3.png",
        name: "新鲜的大白菜",
        introduce: '绿色健康，富含活力花青素',
        weight: '600g',
        price: 3,
        isSelect: false,
      },],
    curNav: 1,
    // curIndex: 0
  },

  //勾选事件处理函数  
  switchSelect: function (e) {
    // 获取item项的id，和数组的下标值  
    var Allprice = 0, i = 0;
    let id = e.target.dataset.id,

      index = parseInt(e.target.dataset.index);
    this.data.carts[index].isSelect = !this.data.carts[index].isSelect;
    //价钱统计
    if (this.data.carts[index].isSelect) {
      this.data.totalMoney = this.data.totalMoney + this.data.carts[index].price;
    }
    else {
      this.data.totalMoney = this.data.totalMoney - this.data.carts[index].price;
    }
 

    //是否全选判断
    for (i = 0; i < this.data.carts.length; i++) {
      Allprice = Allprice + this.data.carts[i].price;
    }
    if (Allprice == this.data.totalMoney) {
      this.data.isAllSelect = true;
    }
    else {
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
    if (!this.data.isAllSelect) {
      for (i = 0; i < this.data.carts.length; i++) {
        this.data.carts[i].isSelect = true;
        this.data.totalMoney = this.data.totalMoney + this.data.carts[i].price;
      }
    }
    else {
      for (i = 0; i < this.data.carts.length; i++) {
        this.data.carts[i].isSelect = false;
      }
      this.data.totalMoney = 0;
    }
    this.setData({
      carts: this.data.carts,
      isAllSelect: !this.data.isAllSelect,
      totalMoney: this.data.totalMoney,
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
    // console.log(typeof(buynum))

    if (buynum == 1) {
      var sItem = "carts[" + ids + "].is_buy";
      this.setData({
        [sItem]: 0,
      })
    } else {
      var buynums = "carts[" + ids + "].buynum";

      this.setData({
        [buynums]: buynum - 1,
      })
    }
  },

  addgoods: function (t) {
    // var type = this.data.curIndex
    var goodid = t.currentTarget.dataset.id
    var buynum = this.data.carts[type].buynum
   
    var buynums = "carts[" + type + "].buynum";

    this.setData({
      [buynums]: buynum + 1,
    })
    // }  
  },

})






