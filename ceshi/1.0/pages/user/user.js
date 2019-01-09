// pages/user/user.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    list1: [
      {type: '待付款', img: '/images/user_page/11.png', path: '/pages/orders/orders?status=1'},
      {type: '待配送', img: '/images/user_page/14.png', path: '/pages/orders/orders?status=2'},
      {type: '待收货', img: '/images/user_page/13.png', path: '/pages/orders/orders?status=3'},
      {type: '待评价', img: '/images/user_page/12.png', path: '/pages/orders/orders?status=4'},
    ],
    list2: [
      {
        type: '美林门店',
        img: '/images/user_page/15.png',
        path: '/pages/store/store',
      },
      {
        type: '美林会员',
        img: '/images/user_page/16.png',
        path: '/pages/member/member',
      },
      {
        type: '兑换优惠券',
        img: '/images/user_page/17.png',
        path: '/pages/coupon/coupon',
      },
      {
        type: '地址',
        img: '/images/user_page/20.png',
        path: '/pages/address/address',
      }
    ],
    list3: [
      {
        type: '我的评价',
        img: '/images/user_page/19.png',
        path: '/pages/evaluate/evaluate'
      },
      {
        type: '邀请好友',
        img: '/images/user_page/18.png',
        path: '/pages/invite/invite'
      },
      {
        type: '预约',
        img: '/images/user_page/21.png',
        path: '/pages/subscribe/subscribe'
      },
      {
        type: '分销中心',
        img: '/images/user_page/22.png',
        path: '/pages/distributor/distributor'
      }
    ]
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