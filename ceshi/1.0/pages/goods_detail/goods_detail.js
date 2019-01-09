// pages/goods_detail/goods_detail.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    show_attr_picker: !1,
    form: {
      number: 1
    },
    goods: {
      attr_pic: "../../images/kind_page/5.png",
      price: 200,
      id: '1',
      original_price: 200
    },
    miaosha_data: {
      miaosha_price: 110,
      rest_num: 1000,
      num: 10,
    },
    attr_group_list: [{
      attr_group_id: 27,
      attr_group_name: "规格",
      attr_list: [{
        attr_id: 72,
        attr_name: "2kg 中果（单果100-120#）"
      }, {
        attr_id: 73,
        attr_name: "2.5kg 大果（单果120#"
      }]
    }],
    imgArr: [
      'http://img.ivsky.com/img/tupian/t/201107/23/baicai-001.jpg',
      'http://img.ivsky.com/img/tupian/t/201107/23/baicai-001.jpg'
    ]
  },
  // 购买弹出
  showRule: function () {
    this.setData({
      isRuleTrue: true
    })
  },
  // 关闭按钮
  hideRule: function () {
    this.setData({
      isRuleTrue: false,
      isRuleShare: false
    })
  },
  //   分享给好友
  onShareAppMessage: function () {
    return this.data.shareData
  },
  // 页面跳转
  navigateUrl: function (e) {
    var url = e.currentTarget.dataset.url;
    url && wx.navigateTo({
      url: url,
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

  },
  goHome (e) {
    wx.switchTab({
      url: "/pages/home/home",
    })
  },
  addCart: function () {
    this.submit("ADD_CART");
  },

  buyNow: function () {
    this.submit("BUY_NOW");
  },

  submit: function (a) {
    var e = this;
    if (!e.data.show_attr_picker) return e.setData({
      show_attr_picker: !0
    }), !0;
    if (e.data.miaosha_data && e.data.miaosha_data.rest_num > 0 && e.data.form.number > e.data.miaosha_data.rest_num) return wx.showToast({
      title: "商品库存不足，请选择其它规格或数量",
      image: "../../images/icon-warning.png"
    }), !0;
    if (e.data.form.number > e.data.goods.num) return wx.showToast({
      title: "商品库存不足，请选择其它规格或数量",
      image: "../../images/icon-warning.png"
    }), !0;
    var i = e.data.attr_group_list, s = [];
    for (var r in i) {
      var n = !1;
      for (var d in i[r].attr_list) if (i[r].attr_list[d].checked) {
        n = {
          attr_id: i[r].attr_list[d].attr_id,
          attr_name: i[r].attr_list[d].attr_name
        };
        break;
      }
      if (!n) return wx.showToast({
        title: "请选择" + i[r].attr_group_name,
        image: "/images/icon-warning.png"
      }), !0;
      s.push({
        attr_group_id: i[r].attr_group_id,
        attr_group_name: i[r].attr_group_name,
        attr_id: n.attr_id,
        attr_name: n.attr_name
      });
    }
    "ADD_CART" == a && (wx.showLoading({
      title: "正在提交",
      mask: !0
    }), o.request({
      url: t.cart.add_cart,
      method: "POST",
      data: {
        goods_id: e.data.id,
        attr: JSON.stringify(s),
        num: e.data.form.number
      },
      success: function (t) {
        wx.showToast({
          title: t.msg,
          duration: 1500
        }), wx.hideLoading(), e.setData({
          show_attr_picker: !1
        });
      }
    })), "BUY_NOW" == a && (e.setData({
      show_attr_picker: !1
    }), wx.redirectTo({
      url: "/pages/order-submit/order-submit?goods_info=" + JSON.stringify({
        goods_id: e.data.id,
        attr: s,
        num: e.data.form.number
      })
    }));
  },

  hideAttrPicker: function () {
    this.setData({
      show_attr_picker: !1
    });
  },

  showAttrPicker: function () {
    this.setData({
      show_attr_picker: !0
    });
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
    a++ , t.setData({
      form: {
        number: a
      }
    });
  },

  numberBlur: function (t) {
    var a = this, o = t.detail.value;
    o = parseInt(o), isNaN(o) && (o = 1), o <= 0 && (o = 1), a.setData({
      form: {
        number: o
      }
    });
  },

  attrClick: function (a) {
    var e = this, i = a.target.dataset.groupId, s = a.target.dataset.id, r = e.data.attr_group_list;
    for (var n in r) if (r[n].attr_group_id == i) for (var d in r[n].attr_list) r[n].attr_list[d].attr_id == s ? r[n].attr_list[d].checked = !0 : r[n].attr_list[d].checked = !1;
    e.setData({
      attr_group_list: r
    });
    var c = [], u = !0;
    for (var n in r) {
      var l = !1;
      for (var d in r[n].attr_list) if (r[n].attr_list[d].checked) {
        c.push(r[n].attr_list[d].attr_id), l = !0;
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
    // }), o.request({
    //   url: t.default.goods_attr_info,
    //   data: {
    //     goods_id: e.data.goods.id,
    //     attr_list: JSON.stringify(c)
    //   },
    //   success: function (t) {
    //     if (wx.hideLoading(), 0 == t.code) {
    //       var a = e.data.goods;
    //       a.price = t.data.price, a.num = t.data.num, a.attr_pic = t.data.pic, e.setData({
    //         goods: a,
    //         miaosha_data: t.data.miaosha
    //       });
    //     }
    //   }
    }));
  },

  goToComment: function(){
    wx.navigateTo({
      url: "/pages/comment/comment?id=" + this.data.goods.id
    });
  },

  previewImg: function (e) {
    // console.log(e.currentTarget.dataset.index);
    var index = e.currentTarget.dataset.index;
    var imgArr = this.data.imgArr;
    // console.log(imgArr[0])
    wx.previewImage({
      current: imgArr[index],     //当前图片地址
      urls: imgArr,               //所有要预览的图片的地址集合 数组形式
      success: function (res) { },
      fail: function (res) { },
      complete: function (res) { },
    })
  }
})