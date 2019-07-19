<template lang="html">
  <section class="pc">
    <article class="plan">
      <blockquote>
        起点：{{msg.startLineInfoBean.lineInfoStart}}<br/>
        终点：{{msg.endLineInfoBean.lineInfoEnd}}<br/>
        {{formatSeconds(msg.lineInfoTimes)}} ￥{{msg.lineInfoPrice}}
      </blockquote>
      <ul v-for="mDetail,index in msg.startLineInfoBean.shortLines">
          <li v-if="mDetail.shortLineType==1"><!--火车-->
            <div class="last">
              <img src="../assets/img/icon/plan/火车.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p>{{mDetail.shortLineVehicleInfo}}</p>
              <p style="color:#862537;font-weight:bold;">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
              <p>{{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}【{{mDetail.shortLineVehicleNum}}】</p>
              <button>购票</button>
            </div>
          </li>
          <li v-if="mDetail.shortLineType==2"><!--飞机-->
            <div class="last">
              <img src="../assets/img/icon/plan/飞机.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p>{{mDetail.shortLineVehicleInfo}}</p>
              <p style="color:#862537;font-weight:bold;">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
              <p>{{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}【{{mDetail.shortLineVehicleNum}}】</p>
              <button>购票</button>
            </div>
          </li>
          <li v-if="mDetail.shortLineType==3"><!--公交-->
            <div class="last">
              <img src="../assets/img/icon/plan/公交.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p>{{mDetail.shortLineVehicleInfo}}</p>
              <p style="color:#862537;font-weight:bold;">
                ￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}
                ({{mDetail.shortLineVehicleTimeTable}})【{{mDetail.shortLineVehicleNum}}】
              </p>
              <p>{{mDetail.shortLineVehicleNum}}——经过{{mDetail.shortLineVehicleSiteNum}}站</p>
            </div>
          </li>
          <li v-if="mDetail.shortLineType==4"><!--驾车-->
            <div class="last">
              <img src="../assets/img/icon/plan/驾车.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p style="color:#862537;font-weight:bold;">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
              <p>{{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}</p>
            </div>
          </li>
          <li v-if="mDetail.shortLineType==5"><!--步行-->
            <div class="last">
              <img src="../assets/img/icon/plan/步行.svg" alt="">
              <span v-if="index==0">{{msg.startLineInfoBean.lineInfoStart}}</span>
              <span v-else>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p>{{mDetail.shortLineVehicleInfo}}</p>
              <p style="color:#862537;font-weight:bold;">用时{{mDetail.shortLineTimes}}</p>
              <p>{{mDetail.shortLineLength}}米</p>
              <button @click="walkMap(mDetail)">步行导航</button>
              <!-- <div id="allmap" v-model="mapview" class="allmap"></div> -->
            </div>
          </li>
          <li v-if="mDetail.shortLineType==6"><!--大巴-->
            <div class="last">
              <img src="../assets/img/icon/plan/大巴.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p>{{mDetail.shortLineVehicleInfo}}</p>
              <p style="color:#862537;font-weight:bold;">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
              <p>{{mDetail.shortLineVehicleNum}}</p>
              <button>购票</button>
            </div>
          </li>
          <li v-if="mDetail.shortLineType==7"><!--高铁-->
            <div class="last">
              <img src="../assets/img/icon/plan/高铁.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p style="color:#862537;font-weight:bold;">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
              <p>{{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}【{{mDetail.shortLineVehicleNum}}】</p>
              <p>{{mDetail.shortLineVehicleInfo}}</p>
              <button>购票</button>
            </div>
          </li>
          <li v-if="mDetail.shortLineType==8"><!--地铁-->
            <div class="last">
              <img src="../assets/img/icon/plan/地铁.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p>{{mDetail.shortLineVehicleInfo}}</p>
              <p style="color:#862537;font-weight:bold;">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
              <p>{{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}【{{mDetail.shortLineVehicleNum}}】</p>
            </div>
          </li>
      </ul>
      <ul v-for="mDetail in msg.shortLines">
          <li v-if="mDetail.shortLineType==1"><!--火车-->
            <div class="last">
              <img src="../assets/img/icon/plan/火车.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p>{{mDetail.shortLineVehicleInfo}}</p>
              <p style="color:#862537;font-weight:bold;">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
              <p>{{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}【{{mDetail.shortLineVehicleNum}}】</p>
              <button>购票</button>
            </div>
          </li>
          <li v-if="mDetail.shortLineType==2"><!--飞机-->
            <div class="last">
              <img src="../assets/img/icon/plan/飞机.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p>{{mDetail.shortLineVehicleInfo}}</p>
              <p style="color:#862537;font-weight:bold;">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
              <p>{{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}【{{mDetail.shortLineVehicleNum}}】</p>
              <button>购票</button>
            </div>
          </li>
          <li v-if="mDetail.shortLineType==3"><!--公交-->
            <div class="last">
              <img src="../assets/img/icon/plan/公交.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p>{{mDetail.shortLineVehicleInfo}}</p>
              <p style="color:#862537;font-weight:bold;">
                ￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}
                ({{mDetail.shortLineVehicleTimeTable}})【{{mDetail.shortLineVehicleNum}}】
              </p>
              <p>{{mDetail.shortLineVehicleNum}}——经过{{mDetail.shortLineVehicleSiteNum}}站</p>
            </div>
          </li>
          <li v-if="mDetail.shortLineType==4"><!--驾车-->
            <div class="last">
              <img src="../assets/img/icon/plan/驾车.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p style="color:#862537;font-weight:bold;">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
              <p>{{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}</p>
            </div>
          </li>
          <li v-if="mDetail.shortLineType==5"><!--步行-->
            <div class="last">
              <img src="../assets/img/icon/plan/步行.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p>{{mDetail.shortLineVehicleInfo}}</p>
              <p style="color:#862537;font-weight:bold;">用时{{mDetail.shortLineTimes}}</p>
              <p>{{mDetail.shortLineLength}}米</p>
              <button @click="walkMap(mDetail)">步行导航</button>
              <!-- <div id="allmap" v-model="mapview" class="allmap"></div> -->
            </div>
          </li>
          <li v-if="mDetail.shortLineType==6"><!--大巴-->
            <div class="last">
              <img src="../assets/img/icon/plan/大巴.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p>{{mDetail.shortLineVehicleInfo}}</p>
              <p style="color:#862537;font-weight:bold;">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
              <p>{{mDetail.shortLineVehicleNum}}</p>
              <button>购票</button>
            </div>
          </li>
          <li v-if="mDetail.shortLineType==7"><!--高铁-->
            <div class="last">
              <img src="../assets/img/icon/plan/高铁.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p style="color:#862537;font-weight:bold;">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
              <p>{{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}【{{mDetail.shortLineVehicleNum}}】</p>
              <p>{{mDetail.shortLineVehicleInfo}}</p>
              <button>购票</button>
            </div>
          </li>
          <li v-if="mDetail.shortLineType==8"><!--地铁-->
            <div class="last">
              <img src="../assets/img/icon/plan/地铁.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p>{{mDetail.shortLineVehicleInfo}}</p>
              <p style="color:#862537;font-weight:bold;">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
              <p>{{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}【{{mDetail.shortLineVehicleNum}}】</p>
            </div>
          </li>
      </ul>
      <ul v-for="mDetail,index in msg.endLineInfoBean.shortLines">
          <li v-if="mDetail.shortLineType==1"><!--火车-->
            <div class="last">
              <img src="../assets/img/icon/plan/火车.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p>{{mDetail.shortLineVehicleInfo}}</p>
              <p style="color:#862537;font-weight:bold;">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
              <p>{{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}【{{mDetail.shortLineVehicleNum}}】</p>
              <button>购票</button>
            </div>
          </li>
          <li v-if="mDetail.shortLineType==2"><!--飞机-->
            <div class="last">
              <img src="../assets/img/icon/plan/飞机.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p>{{mDetail.shortLineVehicleInfo}}</p>
              <p style="color:#862537;font-weight:bold;">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
              <p>{{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}【{{mDetail.shortLineVehicleNum}}】</p>
              <button>购票</button>
            </div>
          </li>
          <li v-if="mDetail.shortLineType==3"><!--公交-->
            <div class="last">
              <img src="../assets/img/icon/plan/公交.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p>{{mDetail.shortLineVehicleInfo}}</p>
              <p style="color:#862537;font-weight:bold;">
                ￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}
                ({{mDetail.shortLineVehicleTimeTable}})【{{mDetail.shortLineVehicleNum}}】
              </p>
              <p>{{mDetail.shortLineVehicleNum}}——经过{{mDetail.shortLineVehicleSiteNum}}站</p>
            </div>
          </li>
          <li v-if="mDetail.shortLineType==4"><!--驾车-->
            <div class="last">
              <img src="../assets/img/icon/plan/驾车.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p style="color:#862537;font-weight:bold;">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
              <p>{{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}</p>
            </div>
          </li>
          <li v-if="mDetail.shortLineType==5"><!--步行-->
            <div class="last">
              <img src="../assets/img/icon/plan/步行.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
              <span v-if="index==0">{{msg.endLineInfoBean.lineInfoStart}}</span>
              <span v-else>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p>{{mDetail.shortLineVehicleInfo}}</p>
              <p style="color:#862537;font-weight:bold;">用时{{mDetail.shortLineTimes}}</p>
              <p>{{mDetail.shortLineLength}}米</p>
              <button @click="walkMap(mDetail)">步行导航</button>
              <!-- <div id="allmap" v-model="mapview" class="allmap"></div> -->
            </div>
          </li>
          <li v-if="mDetail.shortLineType==6"><!--大巴-->
            <div class="last">
              <img src="../assets/img/icon/plan/大巴.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p>{{mDetail.shortLineVehicleInfo}}</p>
              <p style="color:#862537;font-weight:bold;">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
              <p>{{mDetail.shortLineVehicleNum}}</p>
              <button>购票</button>
            </div>
          </li>
          <li v-if="mDetail.shortLineType==7"><!--高铁-->
            <div class="last">
              <img src="../assets/img/icon/plan/高铁.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p style="color:#862537;font-weight:bold;">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
              <p>{{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}【{{mDetail.shortLineVehicleNum}}】</p>
              <p>{{mDetail.shortLineVehicleInfo}}</p>
              <button>购票</button>
            </div>
          </li>
          <li v-if="mDetail.shortLineType==8"><!--地铁-->
            <div class="last">
              <img src="../assets/img/icon/plan/地铁.svg" alt="">
              <span>{{mDetail.shortLineStart}}</span>
            </div>
            <div class="box">
              <p>{{mDetail.shortLineVehicleInfo}}</p>
              <p style="color:#862537;font-weight:bold;">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
              <p>{{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}【{{mDetail.shortLineVehicleNum}}】</p>
            </div>
          </li>
      </ul>
      <!-- 终点 -->
      <div class="last">
        <img src="../assets/img/icon/9终点.svg" alt="">
        <span>{{msg.endLineInfoBean.lineInfoEnd}}</span>
      </div>
    </article>
    <article class="feedback">
      <h2>您的建议永远是我们努力的强大动力</h2>
      <!-- 评价1 -->
    	<ul>
        <li style="line-height: 32px;font-weight:bold">舒适度</li>
        <li v-for="item,index in items"><img :src="item.src" @click="addClass(index)" :class="{active:index==current}"/></li>
    	</ul>
      <!-- 评价2 -->
    	<ul>
        <li style="line-height: 32px;font-weight:bold">价格</li>
    	  <li v-for="item,index in items"><img :src="item.src" @click="addClass2(index)" :class="{active:index==current2}"/></li>
    	</ul>
      <!-- 评价3 -->
    	<ul>
        <li style="line-height: 32px;font-weight:bold">时间</li>
    	  <li v-for="item,index in items"><img :src="item.src" @click="addClass3(index)" :class="{active:index==current3}"/></li>
    	</ul>
    </article>
    <article>
      <textarea class="comment" placeholder="分享你的旅途体验" rows="3" cols='5'></textarea>
      <div style="position:relative;width:88px">
        <img id="loading" style="bottom:0" class="loading" src="../assets/img/icon/loading.gif" alt="加载中……">
        <p id="submitBtn" class="submit" @click="submit">发表评论</p>
      </div>
      <tbody>
        <tr v-for="comment,index in comments[0]">
          <td class="set_title">
            <img style="width:64px;height:64px;" :src="comment.userImgpath"/>{{comment.userUsername}}
          </td>
          <td class="set_title">
            <p>{{comment.content}}</p>
          </td>
          <td class="set_title">
            <div v-if="comment.userId==userObj.userId">
              <span class="btn" @click="deletCom(comment.cid,index)">删除</span>
            </div>
            <div v-else></div>
          </td>
        </tr>
      </tbody>
    </article>
  </section>
</template>

<script>
import {SERVER} from '@/config';
import imgIcon5 from '../assets/img/icon/plan/爱你.svg';
import imgIcon4 from '../assets/img/icon/plan/可爱.svg';
import imgIcon3 from '../assets/img/icon/plan/微笑.svg';
import imgIcon2 from '../assets/img/icon/plan/难过.svg';
import imgIcon1 from '../assets/img/icon/plan/大哭.svg';
export default {
  name: 'feedback',
  data: function(){
    return {
      msg: '',
      mapview: false,
      current: -1,
      current2: -1,
      current3: -1,
      items: [
        {src: imgIcon1},
        {src: imgIcon2},
        {src: imgIcon3},
        {src: imgIcon4},
        {src: imgIcon5}
      ],
      isLogin: '',
      comments: [],
      userObj: '',
      comId: ''
    }
  },
  created(){
    this.isLogin = sessionStorage.getItem('log');

    let msgStr = sessionStorage.getItem('feedback');
    this.msg = JSON.parse(msgStr);

    let user = sessionStorage.getItem('user');
    this.userObj = JSON.parse(user);

    this.getComments();
  },
  methods: {
    // 时间换算
    formatSeconds(value) {
      var secondTime = parseInt(value);// 秒
      var minuteTime = 0;// 分
      var hourTime = 0;// 小时
      if(secondTime > 60) {//如果秒数大于60，将秒数转换成整数
          //获取分钟，除以60取整数，得到整数分钟
          minuteTime = parseInt(secondTime / 60);
          //获取秒数，秒数取佘，得到整数秒数
          secondTime = parseInt(secondTime % 60);
          //如果分钟大于60，将分钟转换成小时
          if(minuteTime > 60) {
              //获取小时，获取分钟除以60，得到整数小时
              hourTime = parseInt(minuteTime / 60);
              //获取小时后取佘的分，获取分钟除以60取佘的分
              minuteTime = parseInt(minuteTime % 60);
          }
      }
      var result = "" + parseInt(secondTime) + "秒";

      if(minuteTime > 0) {
      	result = "" + parseInt(minuteTime) + "分" + result;
      }
      if(hourTime > 0) {
      	result = "" + parseInt(hourTime) + "小时" + result;
      }
      return result;
    },
    //步行导航
    walkMap(mDetail){
      let that=this;
      if (this.mapview) {this.mapview=!this.mapview;}
      let geolocation = new BMap.Geolocation();
      geolocation.getCurrentPosition(function(r){
        if(this.getStatus() == BMAP_STATUS_SUCCESS){
          var map = new BMap.Map("allmap");
          let point = new BMap.Point(r.point);
          map.centerAndZoom(r.point,15);
          map.enableScrollWheelZoom(true);//开启滚动
          var walking = new BMap.WalkingRoute(map, {
              renderOptions: {map: map, autoViewport: true}
          });
          walking.search(mDetail.shortLineStartPoint, mDetail.shortLineEndPoint);
        }
      })
    },
    // 评价
    addClass(index){
      this.current = index;
    },
    addClass2(index){
      this.current2 = index;
    },
    addClass3(index){
      this.current3 = index;
    },
    //得到评论数据
    getComments(){
      let that=this;
      this.axios({
        method: 'post',
        url: SERVER+'traveler/showComment',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        data: {
          routeId: that.msg.lineInfoId
        }
      }).then(function (res) {
        if (res.data.code==1) {
          that.comments.push(res.data.comments);
        }else {
          alert("评论请求失败，请刷新页面");
        }
      }).catch(function (err) {
        console.log(err);
      });
    },
    //发表评论
    submit(){
      let that=this;
      if (that.isLogin!=1) {
        alert("你还没有登陆呢~");
      }else if (that.isLogin==1) {
        $(".loading").css("display","block");
        $("#submitBtn").css("background","transparent");
        $("#submitBtn").css("color","transparent");
        that.axios({
          method: 'post',
          url: SERVER+'traveler/postComment',
          headers: {'Content-Type': 'application/x-www-form-urlencoded'},
          data: {
            comfortableEvaluate: that.current,
            content: $(".comment").val(),
            priceEvaluate: that.current2,
            routeId: that.msg.lineInfoId,
            timeEvaluate: that.current3
          }
        }).then(function (res) {
          if (res.data.code==0) {
            alert(res.data.msg);
            $(".comment").val("");
            $(".loading").css("display","none");
            $("#submitBtn").css("background","#eee");
            $("#submitBtn").css("color","#769164");
          }else if (res.data.code==1) {
            alert(res.data.msg);
            res.data.comment.userImgpath=that.userObj.userImgpath;
            res.data.comment.userUsername=that.userObj.userUsername;
            that.comments[0].unshift(res.data.comment);
            $(".comment").val("");
            that.current=-1;
            that.current2=-1;
            that.current3=-1;
            $(".loading").css("display","none");
            $("#submitBtn").css("background","#eee");
            $("#submitBtn").css("color","#769164");
          }
        }).catch(function (err) {
          console.log(err);
          $(".comment").val("");
          $(".loading").css("display","none");
          $("#submitBtn").css("background","#eee");
          $("#submitBtn").css("color","#769164");
        });
      }
    },
    //删除评论
    deletCom(cid,index){
      let that=this;
      that.axios({
        method: 'post',
        url: SERVER+'traveler/delComment',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        data: {
          cid: cid
        }
      }).then(function (res) {
        if (res.data.code==0) {
          alert(res.data.msg);
        }else if (res.data.code==1) {
          alert(res.data.msg);
          that.comments[0].splice(index);
        }
      }).catch(function (err) {
        console.log(err);
      });
    }
  }
}
</script>

<style lang="css" scoped>
  p{margin: 0;}
  .pc{
    padding-top: 100px;
    padding-bottom: 85px;
    /* background: #555; */
    background: url('../assets/img/bg-pc.jpg');
    background-repeat: no-repeat;
    background-size: cover;
    background-attachment: fixed;
    font-size: 16px;
  }
  .plan{
    padding: 80px;
    border: 20px solid #ddd;
    border-radius: 4px;
    background: #fff;
    color: #000;
  }
  section{
    padding: 170px 190px 40px;
    color: #fff;
  }
  ul{margin: 0;}
  li{list-style: none;}
  .box{
    margin:0;
    width:100%;
    height:100px;
    margin-left: 14px;
    border-left: 3px solid #000;
    position: relative;
  }
	li img,.last>img{
		width: 30px;
		height: 30px;
	}
	li p{padding: 4px 0 0 20px;}
  button{
    position: absolute;
    left: 385px;
    top: 10px;
    width: 88px;
    height: 35px;
    background: #eee;
    border-radius: 5px;
    border: none;
    text-align: center;
    color: #769164;
    font-size: 15px;
    font-weight: bold;
  }
  .allmap{
    width: 600px;
    height: 430px;
    overflow: hidden;
    position: absolute;
    z-index: 99;
    left: 35%;
    top: -74px;
    border-radius: 5px;
  }
  .feedback{margin: 50px 0;}
  .feedback>ul{margin-right: 50px;}
  .feedback>ul>li{
    float: left;
    margin: 10px;
  }
  .feedback li>img:hover, .active{transform: scale(1.5);}
  .comment{
    width: 100%;
    margin: 50px 0 10px;
    border: 2px solid #fff;
    border-radius: 3px;
    color: #555;
    font-size: 16px;
    padding: 20px;
  }
  .submit{
    width: 88px;
    height: 35px;
    background: #eee;
    border-radius: 5px;
    border: none;
    text-align: center;
    line-height: 35px;
    color: #769164;
    font-size: 15px;
    font-weight: bold;
    cursor: pointer;
  }
  .set_title{
    padding: 20px 0;
    width: 20%;
  }
  .btn{
    border: 1px solid #eee;
    color: #eee;
    text-decoration: none;
    padding: 4px 12px;
    font-size: 16px;
    font-weight: 400;
    line-height: normal;
    border-radius: 40px;
    background: none;
  }
  .btn:hover{
    color: #eee;
    background: #42c02e;
    border: 1px solid #42c02e;
  }
</style>
