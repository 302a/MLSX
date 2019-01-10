// pages/home/home.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    shop_arr: [0],
    shop: "丰产路店",
    renqi:[
      { 
        img: "http://59.110.218.60/home_page/2.png",
        title: "红颜草莓300g红颜草莓300g红颜草莓300g红颜草莓300g",
        type: 'first',
        price: "￥28.8"
      },
      {
        img: "http://59.110.218.60/home_page/2.png",
        title: "红颜草莓300g红颜草莓300g红颜草莓300g红颜草莓300g",
        price: "￥28.8"
      },
      {
        img: "http://59.110.218.60/home_page/2.png",
        title: "红颜草莓300g红颜草莓300g红颜草莓300g红颜草莓300g",
        price: "￥28.8"
      },
      {
        img: "http://59.110.218.60/home_page/2.png",
        title: "红颜草莓300g红颜草莓300g红颜草莓300g红颜草莓300g",
        price: "￥28.8"
      },
      {
        img: "http://59.110.218.60/home_page/2.png",
        title: "红颜草莓300g红颜草莓300g红颜草莓300g红颜草莓300g",
        price: "￥28.8",
        type: 'last',
      }
    ]
  },

  showShops: function () {
    var temp = this.data.shop_arr;
    temp.push(this.data.shop_arr.length);
    this.setData({
      shop_arr: temp
    })
  },

  chooseShop: function (e) {
    var temp = this.data.shop_arr;
    console.log(e)
    const shop = e.currentTarget.dataset.title
    temp.pop(this.data.shop_arr.length);
    this.setData({
      shop_arr: temp,
      shop: shop
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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