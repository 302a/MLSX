// pages/submit/submit.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    sub: [{
      time:'9:30',
      name: "生菜",
      weight: "600g",
      jieshao: "营养粗粮，富含活力花青素",
      price: "6.7",
      num: "1",
      isSelect: false,
    }, {
        time: '9:30',
        name: "生菜",
        weight: "600g",
        jieshao: "营养粗粮，富含活力花青素",
        price: "6.7",
        num: "1",
        isSelect: false,
      }, 
    
    ],
    sum:[{
       sumprice:'8.8',
       peisong:3
    }]

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
  }

})