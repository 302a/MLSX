
Page({
  data: {
    cid: 0,
    emptyGoods: 0,
    cat: [
      {id: 1, name: "新鲜水果", ishaveChild: true},
      {id: 2, name: "蔬菜净菜", ishaveChild: true},
      {id: 3, name: "海鲜水产", ishaveChild: true},
      {id: 4, name: "肉禽蛋类", ishaveChild: true},
      {id: 5, name: "粮油副食", ishaveChild: true},
    ],
    banner: [
      {
        page_url: "http://59.110.218.60/pintuan/pintuan",
        title: "元旦",
        pic_url: "http://59.110.218.60/pintuan_page/01.png",
      },
      {
        page_url: "http://59.110.218.60/pintuan/pintuan",
        title: "元旦1",
        pic_url: "http://59.110.218.60/pintuan_page/01.png",
      }],
    // 商品
    goods: ''
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    
    this.setData({
      goods: [
        {
        	id: 15,
        	// 图片地址 
        	cover_pic: "http://59.110.218.60/pintuan_page/02.png",
        	name: "意大利生菜&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;净重250g&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;精选蔬菜",
        	virtual_sales: 256,
        	price: 9.90,
        	original_price: 11.20,
        },
        {
        	id: 14,
        	// 图片地址 
        	cover_pic: "http://59.110.218.60/pintuan_page/04.png",
        	name: "意大利生菜&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;净重250g&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;精选蔬菜",
        	virtual_sales: 568,
        	price: 5.90,
        	original_price: 7.50,
        },
      ]
    })
  },
  switchNav (e) {
  	this.setData({ cid: e.currentTarget.dataset.id})
  	wx.showLoading({
  		title: "正在加载",
  		mask: true
  	});
  	this.setData({
  		goods: [
  			{
  				id: 15,
  				// 图片地址 
  				cover_pic: "http://59.110.218.60/pintuan_page/02.png",
  				name: "意大利生菜&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;净重250g&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;精选蔬菜",
  				virtual_sales: 256,
  				price: 9.90,
  				original_price: 11.20,
  			},
        {
        	id: 13,
        	// 图片地址 
        	cover_pic: "http://59.110.218.60/pintuan_page/03.png",
        	name: "东北糯玉米穗&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;净重200g&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;精选蔬菜",
        	virtual_sales: 99,
        	price: 5.90,
        	original_price: 7.50,
        }
  		]
  	})
  	wx.hideLoading()
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