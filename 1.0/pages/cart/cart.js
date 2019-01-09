// pages/cart/cart.js
Page({


  data: {
    isAllSelect: false,
    totalMoney: 0,
    num:0,
    // 商品详情介绍
    carts: [
      {
        pic: "http://59.110.218.60/cart_page/submit/3.png",
        name: "新鲜的大白菜",
        introduce: '绿色健康，富含活力花青素',
        weight:'600g',
        price: 3,
        isSelect: false,
        // 数据设定
        count: {
          quantity: 2,
          min: 1,
          max: 20
        },
      },
      {
        pic: 'http://59.110.218.60/cart_page/submit/3.png',
        name: "新鲜的大白菜",
        introduce: '绿色健康，富含活力花青素',
        weight: '600g',
        price: 3,
        isSelect: false,
        // 数据设定
        count: {
          quantity: 1,
          min: 1,
          max: 20
        },
      },
      {
        pic: 'http://59.110.218.60/cart_page/submit/3.png',
        name: "新鲜的大白菜",
        introduce:'绿色健康，富含活力花青素',
        weight: '600g',
        price: 3,
        isSelect: false,
        // 数据设定
        count: {
          quantity: 3,
          min: 1,
          max: 20
        },
      },
      {
        pic: 'http://59.110.218.60/cart_page/submit/3.png',
        name: "新鲜的大白菜",
        introduce: '绿色健康，富含活力花青素',
        weight: '600g',
        price: 3,
        isSelect: false,
        // 数据设定
        count: {
          quantity: 1,
          min: 1,
          max: 20
        },
      },
   
      
    ],
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
   bindMinus: function () {

    var num = this.data.num;

    // 如果大于1时，才可以减

    if (num > 1) {

      num--;

    }

    // 只有大于一件的时候，才能normal状态，否则disable状态

    var minusStatus = num <= 1 ? 'disabled' : 'normal';

    // 将数值与状态写回

    this.setData({

      num: num,

      minusStatus: minusStatus

    });

  },

  /* 点击加号 */

  bindPlus: function () {

    var num = this.data.num;

    // 不作过多考虑自增1

    num++;

    // 只有大于一件的时候，才能normal状态，否则disable状态

    var minusStatus = num < 1 ? 'disabled' : 'normal';

    // 将数值与状态写回

    this.setData({

      num: num,

      minusStatus: minusStatus

    });

  },
  /* 输入框事件 */

  bindManual: function (e) {

    var num = e.detail.value;

    // 将数值与状态写回

    this.setData({

      num: num

    });

  }
})



