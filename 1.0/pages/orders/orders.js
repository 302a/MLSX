// pages/orders/orders.js
Page({
  data: {
    currtab: 0,
    swipertab: [
      { name: '全部订单', index: 0 },
      { name: '待付款', index: 1 },
      { name: '待配送', index: 2 },
      { name: '待收货', index: 3 },
      { name: '待评价', index: 4 }
    ],
  },
  onLoad: function (options) {
  },
  getDeviceInfo: function () {
    let that = this
    wx.getSystemInfo({
      success: function (res) {
        that.setData({
          deviceW: res.windowWidth,
          deviceH: res.windowHeight
        })
      }
    })
  },
  onShow: function () {
    this.getDeviceInfo()
    this.orderShow()
  },
  // 点击选项卡 判断是否切换
  tabSwitch: function (e) {
    var that = this
    if (this.data.currtab === e.target.dataset.current) {
      return false
    } else {
      that.setData({
        currtab: e.target.dataset.current
      })
    }
  },
  tabChange: function (e) {
    this.setData({ currtab: e.detail.current })
    this.orderShow()
  },
  orderShow: function () {
    let that = this
    switch (this.data.currtab) {
      case 0:
        that.allorderShow()
        break
      case 1:
        that.waitPayShow()
        break
      case 2:
        that.waitdeliveryShow()
        break
      case 3:
        that.waitreceiveShow()
        break
      case 4:
        that.waitevaluateShow()
    }
  },
  // 全部订单
  allorderShow: function(){
    this.setData({
      allOrder: [
        {name: "草莓", state: "交易成功", time: "2018-09-30 14:00-16:00", status: "已结束", url: "http://59.110.218.60/user_page/01.png", money: "10.9" },
        { name: "西瓜", state: "待付款", time: "2018-10-12 18:00-20:00", status: "未开始", url: "http://59.110.218.60/user_page/01.png", money: "20.9" },
      ]
    })
  },
  // 待付款
  waitPayShow:function(){
  	this.setData({
  		waitPayOrder: [
        { name: "草莓", state: "待付款", time: "2018-10-14 14:00-16:00", url: "http://59.110.218.60/user_page/01.png", money: "10.9" },
        { name: "西瓜", state: "待付款", time: "2018-10-14 14:00-16:00", url: "http://59.110.218.60/user_page/01.png", money: "10.9" }
      ],
  	})
  },
  // 待配送
  waitdeliveryShow: function(){
    this.setData({
      waitDeliveryOrder: [
        { name: "草莓", state: "待配送", time: "2018-10-14 14:00-16:00", url: "http://59.110.218.60/user_page/01.png", money: "10.9" },
        { name: "草莓", state: "待收货", time: "2018-10-14 14:00-16:00", url: "http://59.110.218.60/user_page/01.png", money: "10.9" },
      ]
    })
  },
  // 待收货
  waitreceiveShow: function () {
    this.setData({
      waitReceiveOrder: [
        { name: "草莓", state: "待收货", time: "2018-10-14 14:00-16:00", url: "http://59.110.218.60/user_page/01.png", money: "10.9" },
        { name: "草莓", state: "待收货", time: "2018-10-14 14:00-16:00", url: "http://59.110.218.60/user_page/01.png", money: "10.9" }
      ],
    })
  },
  // 待评价
  waitevaluateShow : function () {
    this.setData ({
       waitEvaluateOrder: [
         {name: "草莓", state: "待评价", time: "2018-10-4 10:00-12:00", url: "http://59.110.218.60/user_page/01.png", money: "8.8" },
         {name: "草莓", state: "待评价", time: "2018-10-4 10:00-12:00", url: "http://59.110.218.60/user_page/01.png", money: "8.8" }
      ]
    })
  },
  // 去评价
  goEvaluate () {
    wx.navigateTo({
      url:"/pages/evaluate/evaluate"
    })
  },
  // 去支付
  goPay () {
    wx.navigateTo({
      url: "/pages/pay-success/pay-success"
    })
  },
  // 去收货
  goReceive () {
    wx.navigateTo({
      url: "/pages/receive-success/receive-success"
    })
  },
  onReady: function () {},
  onHide: function () {},
  onUnload: function () {},
  onPullDownRefresh: function () {},
  onShareAppMessage: function () {}
})