// pages/pay-mumber/pay-mumber.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    id: 0,
    payPrice: 8,
    list: [
      {time: 1, price: 8, select: false},
      {time: 3, price: 18, select: true},
      {time: 6, price: 30, select: true},
      {time: 12, price: 48, select: true}
    ]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },
  // 切换
  isSelect (e) {
    // console.log(e.currentTarget.dataset.price)
    var index = e.currentTarget.dataset.index
    var price = 
    this.setData({
      id: index,
      payPrice: e.currentTarget.dataset.price
    })
  },
  pay () {
    wx.showToast({
      title: '支付成功',
    	icon: 'success',
      duration: 1000
    })
  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})