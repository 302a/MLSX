var a = getApp();

Page({
  data: {
    priceclick: 0,
    priceimg: [
      'http://59.110.218.60/images/kind_page/icon-sort-up.png',
      'http://59.110.218.60/images/kind_page/icon-sort-down.png',
    ],
    cateItems: [
      {
        cate_id: 1,
        cate_name: "水果",
        ishaveChild: true,
        children:
          [
            {
              child_id: 1,
              is_buy: 0,
              buynum: 1,
              name: '樱桃',
              image: "https://m.360buyimg.com/mobilecms/s357x357_jfs/t15613/296/2281640440/392160/6e019064/5a9a450dNa47bf95f.jpg!q50.jpg",
              price: '12.5',
              height: '净重35g',
              descripe: '口感微妙，轻咬鲜嫩多汁回味微苦'
            },
            {
              child_id: 2,
              is_buy: 0,
              buynum: 1,
              name: '樱桃',
              image: "https://m.360buyimg.com/mobilecms/s357x357_jfs/t15613/296/2281640440/392160/6e019064/5a9a450dNa47bf95f.jpg!q50.jpg",
              price: '12.5',
              height: '净重35g',
              descripe: '口感微妙，轻咬鲜嫩多汁回味微苦'
            },
            {
              child_id: 3,
              is_buy: 0,
              buynum: 1,
              name: '樱桃',
              image: "https://m.360buyimg.com/mobilecms/s357x357_jfs/t15613/296/2281640440/392160/6e019064/5a9a450dNa47bf95f.jpg!q50.jpg",
              price: '12.5',
              height: '净重35g',
              descripe: '口感微妙，轻咬鲜嫩多汁回味微苦'
            },
            {
              child_id: 4,
              is_buy: 0,
              buynum: 1,
              name: '樱桃',
              image: "https://m.360buyimg.com/mobilecms/s357x357_jfs/t15613/296/2281640440/392160/6e019064/5a9a450dNa47bf95f.jpg!q50.jpg",
              price: '12.5',
              height: '净重35g',
              descripe: '口感微妙，轻咬鲜嫩多汁回味微苦'
            }
          ]
      },
      {
        cate_id: 2,
        cate_name: "干果",
        ishaveChild: true,
        children:
          [
            {
              child_id: 1,
              is_buy: 0,
              buynum: 1,
              name: '夏威夷果',
              image: "https://m.360buyimg.com/mobilecms/s357x357_jfs/t18901/57/1522219067/198105/1f4ad39/5acaccb2Nf4a6792b.jpg!q50.jpg",
              price: '12.5',
              height: '净重35g',
              descripe: '口感微妙，轻咬鲜嫩多汁回味微苦'
            },
            {
              child_id: 2,
              is_buy: 0,
              buynum: 1,
              name: '夏威夷果',
              image: "https://m.360buyimg.com/mobilecms/s357x357_jfs/t18901/57/1522219067/198105/1f4ad39/5acaccb2Nf4a6792b.jpg!q50.jpg",
              price: '12.5',
              height: '净重35g',
              descripe: '口感微妙，轻咬鲜嫩多汁回味微苦'
            },
            {
              child_id: 3,
              is_buy: 0,
              buynum: 1,
              name: '夏威夷果',
              image: "https://m.360buyimg.com/mobilecms/s357x357_jfs/t18901/57/1522219067/198105/1f4ad39/5acaccb2Nf4a6792b.jpg!q50.jpg",
              price: '12.5',
              height: '净重35g',
              descripe: '口感微妙，轻咬鲜嫩多汁回味微苦'
            },
            {
              child_id: 4,
              is_buy: 0,
              buynum: 1,
              name: '夏威夷果',
              image: "https://m.360buyimg.com/mobilecms/s357x357_jfs/t18901/57/1522219067/198105/1f4ad39/5acaccb2Nf4a6792b.jpg!q50.jpg",
              price: '12.5',
              height: '净重35g',
              descripe: '口感微妙，轻咬鲜嫩多汁回味微苦'
            },
            {
              child_id: 5,
              is_buy: 0,
              buynum: 1,
              name: '夏威夷果',
              image: "https://m.360buyimg.com/mobilecms/s357x357_jfs/t18901/57/1522219067/198105/1f4ad39/5acaccb2Nf4a6792b.jpg!q50.jpg",
              price: '12.5',
              height: '净重35g',
              descripe: '口感微妙，轻咬鲜嫩多汁回味微苦'
            },
            {
              child_id: 6,
              is_buy: 0,
              buynum: 1,
              name: '夏威夷果',
              image: "https://m.360buyimg.com/mobilecms/s357x357_jfs/t18901/57/1522219067/198105/1f4ad39/5acaccb2Nf4a6792b.jpg!q50.jpg",
              price: '12.5',
              height: '净重35g',
              descripe: '口感微妙，轻咬鲜嫩多汁回味微苦'
            },
            {
              child_id: 7,
              is_buy: 0,
              buynum: 1,
              name: '夏威夷果',
              image: "https://m.360buyimg.com/mobilecms/s357x357_jfs/t18901/57/1522219067/198105/1f4ad39/5acaccb2Nf4a6792b.jpg!q50.jpg",
              price: '12.5',
              height: '净重35g',
              descripe: '口感微妙，轻咬鲜嫩多汁回味微苦'
            },
            {
              child_id: 8,
              is_buy: 0,
              buynum: 1,
              name: '夏威夷果',
              image: "https://m.360buyimg.com/mobilecms/s357x357_jfs/t18901/57/1522219067/198105/1f4ad39/5acaccb2Nf4a6792b.jpg!q50.jpg",
              price: '12.5',
              height: '净重35g',
              descripe: '口感微妙，轻咬鲜嫩多汁回味微苦'
            }
          ]
      },
      {
        cate_id: 3,
        cate_name: "蔬菜",
        ishaveChild: true,
        children:
          [
            {
              child_id: 1,
              is_buy: 0,
              buynum: 1,
              name: '有机上海青',
              image: "https://m.360buyimg.com/mobilecms/s357x357_jfs/t2827/290/2563889921/292001/bf218791/576b843eN1f7e4b44.jpg!q50.jpg"
            },
            {
              child_id: 2,
              is_buy: 0,
              buynum: 1,
              name: '有机上海青',
              image: "https://m.360buyimg.com/mobilecms/s357x357_jfs/t2827/290/2563889921/292001/bf218791/576b843eN1f7e4b44.jpg!q50.jpg"
            },
            {
              child_id: 3,
              is_buy: 0,
              buynum: 1,
              name: '有机上海青',
              image: "https://m.360buyimg.com/mobilecms/s357x357_jfs/t2827/290/2563889921/292001/bf218791/576b843eN1f7e4b44.jpg!q50.jpg"
            },
            {
              child_id: 4, 
              is_buy: 0,
              buynum: 1,
              name: '有机上海青',
              image: "https://m.360buyimg.com/mobilecms/s357x357_jfs/t2827/290/2563889921/292001/bf218791/576b843eN1f7e4b44.jpg!q50.jpg"
            }
          ]
      },
      {
        cate_id: 4,
        is_buy: 0,
        cate_name: "海鲜",
        ishaveChild: false,
        children: []
      }
    ],
    curNav: 1,
    curIndex: 0
  },

  onShow:function(e){
    var t = this
    t.getgoods();
  },

  //事件处理函数  
  switchRightTab: function (e) {
    // 获取item项的id，和数组的下标值  
    let id = e.target.dataset.id,
      index = parseInt(e.target.dataset.index);
    // 把点击到的某一项，设为当前index  
    this.setData({
      curNav: id,
      curIndex: index
    })
  },

  sort_price: function(){
    var e = this
    var priceclick = e.data.priceclick
    if(priceclick=='0'){
      e.setData({
        priceclick: !priceclick,
        priceimg: [
          'http://59.110.218.60/images/kind_page/icon-sort-up-active.png',
          'http://59.110.218.60/images/kind_page/icon-sort-down.png',
        ]
      });
    }if(priceclick=='1'){
      e.setData({
        priceclick: !priceclick,
        priceimg: [
          'http://59.110.218.60/images/kind_page/icon-sort-up.png',
          'http://59.110.218.60/images/kind_page/icon-sort-down-active.png',
        ]
      });
    }
  },

  allClick: function () {
    var t = this 
    var a = t.data.cat_list;
    for (var e in a) {
      for (var i in a[e].list) a[e].list[i].checked = !1;
      a[e].checked = !1;
    }
    t.setData({
      cat_list: a,
      cat_id: "",
      height_bar: ""
    }), t.reloadGoodsList();
  },

  catClick: function (t) {
    var a = this
    var e = "", i = t.currentTarget.dataset.index, s = a.data.cat_list;
    for (var o in s) {
      for (var r in s[o].list) s[o].list[r].checked = !1;
      o == i ? (s[o].checked = !0, e = s[o].id) : s[o].checked = !1;
    }
    var d = "";
    s[i].list.length > 0 && (d = "height-bar"), a.setData({
      cat_list: s,
      cat_id: e,
      height_bar: d
    }), a.reloadGoodsList();
  },

  subCatClick: function (t) {
    var a = this, e = "", i = t.currentTarget.dataset.index, s = t.currentTarget.dataset.parentIndex, o = a.data.cat_list;
    for (var r in o) for (var d in o[r].list) r == s && d == i ? (o[r].list[d].checked = !0,
      e = o[r].list[d].id) : o[r].list[d].checked = !1;
    a.setData({
      cat_list: o,
      cat_id: e
    }), a.reloadGoodsList();
  },

  sortClick: function (t) {
    var a = this, e = t.currentTarget.dataset.sort, i = void 0 == t.currentTarget.dataset.default_sort_type ? -1 : t.currentTarget.dataset.default_sort_type, s = a.data.sort_type;
    if (a.data.sort == e) {
      if (-1 == i) return;
      s = -1 == a.data.sort_type ? i : 0 == s ? 1 : 0;
    } else s = i;
    a.setData({
      sort: e,
      sort_type: s
    }), a.reloadGoodsList();
  },

  reloadGoodsList: function () {
    var e = this;
    var i = !1
    e.setData({
      page: 1,
      goods_list: [],
      show_no_data_tip: !1
    });
    var s = e.data.cat_id || "", o = e.data.page || 1;
    a.request({
      url: t.default.goods_list,
      data: {
        cat_id: s,
        page: o,
        sort: e.data.sort,
        sort_type: e.data.sort_type
      },
      success: function (t) {
        0 == t.code && (0 == t.data.list.length && (i = !0), e.setData({
          page: o + 1
        }), e.setData({
          goods_list: t.data.list
        })), e.setData({
          show_no_data_tip: 0 == e.data.goods_list.length
        });
      },
      complete: function () { }
    });
  },

  addTocart: function(t){
    var type = this.data.curIndex
    // console.log(type)
    var goodid = t.currentTarget.dataset.id
    var ids = parseInt(goodid) - 1
    var array = this.data.cateItems
    var sItem = "cateItems[" + type + "].children[" + ids + "].is_buy";

    // array.forEach((item, index, arr) => {
    //   var sItem = "cateItems[" + index + "].children["+index+"]";
    //   this.setData({
    //     [sItem]: " "
    //   })
    //   console.log([sItem]);
    // })

    this.setData({
      [sItem]: 1,
    })

  },

  subgoods: function(t){
    var type = this.data.curIndex
    var goodid = t.currentTarget.dataset.id
    var ids = parseInt(goodid) - 1
    var buynum = this.data.cateItems[type].children[ids].buynum
    // console.log(typeof(buynum))

    if (buynum == 1) {
      var sItem = "cateItems[" + type + "].children[" + ids + "].is_buy";
      this.setData({
        [sItem]: 0,
      })
    }else{
      var buynums = "cateItems[" + type + "].children[" + ids + "].buynum";

      this.setData({
        [buynums]: buynum - 1,
      })
    }  
  },

  addgoods: function(t){
    var type = this.data.curIndex
    var goodid = t.currentTarget.dataset.id
    var ids = parseInt(goodid) - 1
    var buynum = this.data.cateItems[type].children[ids].buynum
    // console.log(typeof(buynum))

    // if (buynum == 1) {
    //   var sItem = "cateItems[" + type + "].children[" + ids + "].is_buy";
    //   this.setData({
    //     [sItem]: 0,
    //   })
    // } else {
      var buynums = "cateItems[" + type + "].children[" + ids + "].buynum";

      this.setData({
        [buynums]: buynum + 1,
      })
    // }  
  },

  myCatchTouch: function () {
    console.log('stop user scroll it!');
    return;
  },

  getgoods: function () {
    var e = this
    wx.request({
      url: 'http://localhost:8000/mlsx/send_goods/',
      method: 'GET',
      header: {
        "content-type": "application/json;charset=UTF-8"
      },
      success: function (t) {
        // console.log(t.data.content)
        e.setData({
          cateItems: [
            t.data.content
          ]
        })
        var cateItems = e.data.cateItems
        console.log(cateItems)
      }
    })
  }
})
