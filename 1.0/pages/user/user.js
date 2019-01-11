// pages/user/user.js
Page({
  /**
   * 页面的初始数据
   */
  data: {
    cid: 1,
    list1: [
      { type: '待付款', img: 'http://59.110.218.60/images/user_page/123.png', path: '/pages/orders/orders?status=1'},
      { type: '待配送', img: 'http://59.110.218.60/images/user_page/456.png', path: '/pages/orders/orders?status=2'},
      { type: '待收货', img: 'http://59.110.218.60/images/user_page/789.png', path: '/pages/orders/orders?status=3'},
      { type: '待评价', img: 'http://59.110.218.60/images/user_page/0012.png', path: '/pages/orders/orders?status=4'},
    ],
    list2: [
      {
        type: '美林门店',
        img: 'http://59.110.218.60/images/user_page/11111.png',
        path: '/pages/store/store',
      },
      {
        type: '美林会员',
        img: 'http://59.110.218.60/images/user_page/222222.png',
        path: '/pages/member/member',
      },
      {
        type: '兑换优惠券',
        img: 'http://59.110.218.60/images/user_page/33333.png',
        path: '/pages/coupon/coupon',
      }
    ],
    list3: [
      {
        type: '我的评价',
        img: 'http://59.110.218.60/images/user_page/365287.png',
        path: '/pages/evaluate/evaluate'
      },
      {
        type: '邀请好友',
        img: 'http://59.110.218.60/images/user_page/896547.png',
        path: '/pages/invite/invite'
      },
      {
        type: '预约',
        img: 'http://59.110.218.60/images/user_page/56982.png',
        path: '/pages/subscribe/subscribe'
      },
      {
        type: '分销中心',
        img: 'http://59.110.218.60/images/user_page/2356987.png',
        path: '/pages/distributor/distributor'
      }
    ]
  },
  address () {
    if (wx.chooseAddress) {
      wx.chooseAddress({
      	success (res) {
      		console.log(res.userName)
      		console.log(res.postalCode)
      		console.log(res.provinceName)
      		console.log(res.cityName)
      		console.log(res.countyName)
      		console.log(res.detailInfo)
      		console.log(res.nationalCode)
      		console.log(res.telNumber)
      	},
        fail (err) {
        	console.info("收货地址授权失败");
        	wx.showToast({
        		title: '授权失败，您将无法进行下单支付',
        		icon: 'none',
        		duration: 2000
        	})
        }
      })
    } else {
      console.log('当前微信版本不支持chooseAddress');
    }
  },
  pay_mumber () {
    wx.navigateTo({
    	url: '/pages/pay-mumber/pay-mumber'
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