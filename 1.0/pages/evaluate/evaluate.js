// pages/evaluate/evaluate.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    userStars1: ['http://59.110.218.60/evaluate_page/03.png', 'http://59.110.218.60/evaluate_page/03.png', 'http://59.110.218.60/evaluate_page/03.png', 'http://59.110.218.60/evaluate_page/03.png', 'http://59.110.218.60/evaluate_page/03.png'],
    userStars2: ['http://59.110.218.60/evaluate_page/03.png', 'http://59.110.218.60/evaluate_page/03.png', 'http://59.110.218.60/evaluate_page/03.png', 'http://59.110.218.60/evaluate_page/03.png', 'http://59.110.218.60/evaluate_page/03.png'],
    userStars3: ['http://59.110.218.60/evaluate_page/03.png', 'http://59.110.218.60/evaluate_page/03.png', 'http://59.110.218.60/evaluate_page/03.png', 'http://59.110.218.60/evaluate_page/03.png', 'http://59.110.218.60/evaluate_page/03.png'],
    flag: true
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },
  // 花朵点击事件
  starTap1: function(e){
    var index = e.currentTarget.dataset.index; // 获取当前点击的是第几个
    var tempUserStars = this.data.userStars1; // 暂存花朵数组
    var len = tempUserStars.length; // 获取花朵数组的长度
    for(var i = 0; i < len; i ++){
      if(i <= index){ // 小于等于index的是满心
        tempUserStars[i] = 'http://59.110.218.60/evaluate_page/07.png'
      }else{ // 其他是空心
        tempUserStars[i] = 'http://59.110.218.60/evaluate_page/03.png'
      }
    }
    // 重新赋值就可以显示了
    this.setData({
        userStars1: tempUserStars
    })
  },
  starTap2: function(e){
  	var index = e.currentTarget.dataset.index;
  	var tempUserStars = this.data.userStars2;
  	var len = tempUserStars.length;
  	for(var i = 0; i < len; i ++){
  		if(i <= index){
  			tempUserStars[i] = 'http://59.110.218.60/evaluate_page/07.png'
  		}else{
  			tempUserStars[i] = 'http://59.110.218.60/evaluate_page/03.png'
  		}
  	}
  	this.setData({
  			userStars2: tempUserStars
  	})
  },
  starTap3: function(e){
  	var index = e.currentTarget.dataset.index;
  	var tempUserStars = this.data.userStars3;
  	var len = tempUserStars.length;
  	for(var i = 0; i < len; i ++){
  		if(i <= index){
  			tempUserStars[i] = 'http://59.110.218.60/evaluate_page/07.png'
  		}else{
  			tempUserStars[i] = 'http://59.110.218.60/evaluate_page/03.png'
  		}
  	}
  	this.setData({
        userStars3: tempUserStars
  	})
  },
  // 点击发布 跳转
  evaluateSuccess () {
    wx.navigateTo({
      url:"/pages/evaluate-success/evaluate-success"
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