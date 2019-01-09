// pages/pintuan_details/pintuan_details.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    show_attr_picker: !1,
    form: {
      number: 1
    },
    reduce_price: 0.30,
    comment_num: 0,
    goods: {
      name: "意大利生菜&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;净重250g&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;精选蔬菜",
      price: 9.90,
      num: 120,
      id: '1',
      original_price: 11.20,
      group_num: 21,
      virtual_sales: 11,
    },
    attr_group_list: [{
      attr_group_id: 27,
      attr_group_name: "规格",
      attr_list: [{
        attr_id: 72,
        attr_name: "250g   意大利生菜"
      },
      {
      attr_id: 73,
      attr_name: "240g   意大利生菜"
      }]
    }],

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
  goHome: function() {
    wx.switchTab({
      url: '/pages/pintuan/pintuan'
    });
  },
  goToComment: function (t) {
    wx.showModal({
      title: '提示',
      content: '暂无评价',
    });
  },
  hideAttrPicker: function () {
    this.setData({
      show_attr_picker: !1
    });
  },
  call_phone: function () {
    wx
  },
  showAttrPicker: function () {
    this.setData({
      show_attr_picker: !0
    });
  },
  buyNow: function () {
    this.submit("GROUP_BUY");
  },
  onlyBuy: function () {
    this.submit("ONLY_BUY");
  },
  attrClick: function (t) {
    var a = this, o = t.target.dataset.groupId, r = t.target.dataset.id, n = a.data.attr_group_list;
    for (var s in n) if (n[s].attr_group_id == o) for (var d in n[s].attr_list) n[s].attr_list[d].attr_id == r ? n[s].attr_list[d].checked = !0 : n[s].attr_list[d].checked = !1;
    a.setData({
      attr_group_list: n
    });
    var c = [], u = !0;
    for (var s in n) {
      var l = !1;
      for (var d in n[s].attr_list) if (n[s].attr_list[d].checked) {
        c.push(n[s].attr_list[d].attr_id), l = !0;
        break;
      }
      if (!l) {
        u = !1;
        break;
      }
    }
    u && (wx.showLoading({
      title: "正在加载",
      mask: !0
    }), i.request({
      url: e.group.goods_attr_info,
      data: {
        goods_id: a.data.goods.id,
        attr_list: JSON.stringify(c)
      },
      success: function (t) {
        if (wx.hideLoading(), 0 == t.code) {
          var e = a.data.goods;
          e.price = t.data.price, e.num = t.data.num, e.attr_pic = t.data.pic, e.original_price = t.data.single,
            a.setData({
              goods: e
            });
        }
      }
    }));
  },
  numberSub: function () {
    var t = this, a = t.data.form.number;
    if (a <= 1) return !0;
    a-- , t.setData({
      form: {
        number: a
      }
    });
  },
  numberAdd: function () {
    var t = this, a = t.data.form.number;
    ++a > t.data.goods.one_buy_limit && 0 != t.data.goods.one_buy_limit ? wx.showModal({
      title: "提示",
      content: "数量超过最大限购数",
      showCancel: !1,
      success: function (t) { }
    }) : t.setData({
      form: {
        number: a
      }
    });
  },
})