Page({

  data: {
    flag: true,
    Select: false,
    totalMoney: '', // 商品总额
    num: 0,
    cart_id: 1,
    paymoney: '', // 商品实付
    sendmoney: 3,
    // 商品详情介绍
    carts: [{
      id: 1,
      buynum: 1,
      pic: "http://59.110.218.60/images/cart_page/submit/3.png",
      name: "新鲜的大白菜",
      introduce: '绿色健康，富含活力花青素',
      weight: '600g',
      price: 2,
    },
    {
      id: 2,
      buynum: 2,
      pic: "http://59.110.218.60/images/cart_page/submit/3.png",
      name: "新鲜的大白菜",
      introduce: '绿色健康，富含活力花青素',
      weight: '600g',
      price: 2,
    },
    {
      id: 3,
      buynum: 3,
      pic: "http://59.110.218.60/images/cart_page/submit/3.png",
      name: "新鲜的大白菜",
      introduce: '绿色健康，富含活力花青素',
      weight: '600g',
      price: 2,
    }
    ]
  },
  // 选地址
  address () {
  	if (wx.chooseAddress) {
  		wx.chooseAddress({
  			success:(res) => {
          console.log(res)
          this.setData({
          	addressInfo: res,
            flag: false
          })
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
  // 
  isSelect () {
    wx.navigateTo({
    	url: "/pages/pay-mumber/pay-mumber"
    })
    this.setData({
      Select: !this.data.Select
    })
  },
  // 计算总价
  onShow: function(options) {
    var totalMoney = 0
    for (var i = 0;i < this.data.carts.length; i++){
      totalMoney = totalMoney + this.data.carts[i].buynum * this.data.carts[i].price
      // console.log(totalMoney)
    }
    this.setData({
      totalMoney: totalMoney,
      paymoney: totalMoney + this.data.sendmoney
    })
  },
  // 去支付
  toBuy() {
    wx.showToast({
      title: '支付成功',
      icon: 'success',
      duration: 3000,
      success: function () {
        wx.navigateTo({
        	url: "/pages/pay-success/pay-success"
        })
      }
    });
  },
  //字数限制  
  inputs: function (e) {
    // 获取输入框的内容
    var value = e.detail.value;
    // 获取输入框内容的长度
    var len = parseInt(value.length);
    //最多字数限制
    if(len > this.data.max) return;
    // 当输入框内容的长度大于最大长度限制（max)时，终止setData()的执行
      this.setData({
         currentWordNumber: len //当前字数
      });
    }
})