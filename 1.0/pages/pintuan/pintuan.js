// pages/pintuan/pintuan.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    cid: 0,
    cat: [
      {
      id: 8,
      name: "新鲜水果",
      ishaveChild: true, 
      },
      {
      id: 10,
      name: "蔬菜净菜",
      },
      {
      id: 11,
      name: "海鲜水产",
      },
      {
      id: 12,
      name: "肉禽蛋类",
      },
      {
      id: 13,
      name: "粮油副食",
      }],
    banner: [
      {
        page_url: "/pages/pintuan/pintuan",
        title: "元旦",
        pic_url: "../../images/pintuan_page/01.png",
      },
      {
        page_url: "/pages/pintuan/pintuan",
        title: "元旦1",
        pic_url: "../../images/pintuan_page/01.png",
      }],
    // 商品
    goods: [
      {
        id: 12, 
        // 图片地址 
        cover_pic: "/images/pintuan_page/02.png",
        name: "意大利生菜&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;净重250g&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;精选蔬菜",
        virtual_sales: 256,
        price: 4.34,
        original_price: 5.60,
      },
      {
        id: 13,
        // 图片地址 
        cover_pic: "/images/pintuan_page/03.png",
        name: "东北糯玉米穗&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;净重200g&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;精选蔬菜",
        virtual_sales: 99,
        price: 5.90,
        original_price: 7.50,
      },{
        id: 14,
        // 图片地址 
        cover_pic: "/images/pintuan_page/04.png",
        name: "意大利生菜&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;净重250g&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;精选蔬菜",
        virtual_sales: 568,
        price: 3.80,
        original_price: 6.90,
      },
      {
        id: 15,
        // 图片地址 
        cover_pic: "/images/pintuan_page/02.png",
        name: "意大利生菜&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;净重250g&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;精选蔬菜",
        virtual_sales: 256,
        price: 4.34,
        original_price: 5.60,
      }]
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

  },
  switchNav: function (o) {
    var e = this;
    wx.showLoading({
      title: "正在加载",
      mask: !0
    });
    var n = 0;
    if (n != o.currentTarget.dataset.id || 0 == o.currentTarget.dataset.id) {
      n = o.currentTarget.dataset.id, console.log(this.systemInfo);
      var s = this.systemInfo.windowWidth, d = o.currentTarget.offsetLeft, r = this.data.scrollLeft;
      r = d > s / 2 ? d : 0, e.setData({
        cid: n,
        page: 1,
        scrollLeft: r,
        scrollTop: 0,
        emptyGoods: 0,
        goods: [],
        show_loading_bar: 1
      }), t.request({
        url: a.group.list,
        method: "get",
        data: {
          cid: n
        },
        success: function (a) {
          if (0 == a.code) {
            setTimeout(function () {
              wx.hideLoading();
            }, 1e3);
            var t = a.data.list;
            a.data.page_count >= a.data.page ? e.setData({
              goods: t,
              page: a.data.page,
              page_count: a.data.page_count,
              row_count: a.data.row_count,
              show_loading_bar: 0
            }) : e.setData({
              emptyGoods: 1
            });
          }
        }
      });
    }
  },
})