<template lang="html">
  <section>
    <div class="pc" v-if="flag">
      <div id="allmap1"></div>
      <div id="allmap2"></div>
      <div class="container-fluid search_box">
        <div class="row">
          <div class="col-lg-3 input-group">
            <input type="text" id="locate" class="form-control" placeholder="起始地">
            <span class="input-group-addon" @click="position">
              <span class="glyphicon glyphicon-map-marker" id="icon" aria-hidden="true"></span>
            </span>
          </div>
          <div class="col-lg-3 input-group">
            <input type="text" id="locate2" class="form-control" placeholder="目的地">
            <span class="input-group-addon" @click="position2">
              <span class="glyphicon glyphicon-map-marker" id="icon2" aria-hidden="true"></span>
            </span>
          </div>
          <div class="col-lg-2 input-group"  @click="getCalendar" style="position: relative;">
            <input readonly="readonly" type="text" v-model="msgDate" id="time" class="form-control" placeholder="yyyy-mm-dd">
            <span class="input-group-addon"><span class="glyphicon glyphicon-calendar" aria-hidden="true"></span></span>
            <Calendar  class="calendar" v-show="calFlag"
                v-on:choseDay="clickDay"
                :sundayStart="true"
            ></Calendar>
          </div>
          <div class="col-lg-2 buju" @click="getAccurateTime">
            <TimePicker v-on:hour="hour" v-on:minute="minute" v-on:timeHour="timeHour" v-on:timeMinute="timeMinute"/>
          </div>
          <div class="col-lg-2 buju"  @click="search">
            <img id="loading" class="loading" src="../assets/img/icon/loading.gif" alt="加载中……">
            <div class="form-item"><a class="btn"> 查询 </a></div>
          </div>
        </div>
    	</div>
      <!-- 方案 -->
      <div class="routes" v-for="mMsg,index in msg">
    		<p>方案推荐</p>
    		<div class="tips">
          <div class="detail_info">
            <blockquote>
              起点：{{mMsg.lineInfoStart}}<br/>
              终点：{{mMsg.lineInfoEnd}}<br/>
              <!-- 总时间：{{mMsg.lineInfoTimes}} -￥{{mMsg.lineInfoPrice}} -->
              总时间：{{formatSeconds(mMsg.lineInfoTimes)}}
            </blockquote>
            <ul v-for="mDetail in mMsg.oneCityShortLineList">
              <li v-if="mDetail.shortLineType==1"><!--火车-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/火车.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}——用时{{mDetail.timesStr}}</p>
                  <p>{{mDetail.startTime}}-{{mDetail.endTime}}-{{mDetail.shortLineVehicleNum}}</p>
                </div>
              </li>
              <li v-if="mDetail.shortLineType==2"><!--飞机-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/飞机.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}——用时{{mDetail.timesStr}}</p>
                  <p>{{mDetail.shortLineVehicleTimeTable}}【{{mDetail.shortLineVehicleNum}}】</p>
                </div>
              </li>
              <li v-if="mDetail.shortLineType==3"><!--公交-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/公交.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}—用时{{mDetail.timesStr}}</p>
                  <p style="color:#416367;font-weight:bold;margin:0">【{{mDetail.shortLineVehicleNum}}】</p>
                  <p style="color:#416367;font-weight:bold;">{{mDetail.shortLineVehicleTimeTable}}</p>
                </div>
              </li>
              <li v-if="mDetail.shortLineType==4"><!--驾车-->
                <p style="color:#862537;font-weight:bold;">￥{{mDetail.shortLinePrice}}——用时{{mDetail.timesStr}}</p>
                <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                <p>{{mDetail.shortLineVehicleTimeTable}}</p>
              </li>
              <li v-if="mDetail.shortLineType==5"><!--步行-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/步行.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">用时{{mDetail.timesStr}}</p>
                  <p style="color:#416367;font-weight:bold;">{{mDetail.shortLineVehicleInfo}}</p>
                </div>
              </li>
              <li v-if="mDetail.shortLineType==6"><!--大巴-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/大巴.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}——用时{{mDetail.timesStr}}</p>
                  <p style="color:#416367;font-weight:bold;">【{{mDetail.shortLineVehicleNum}}】{{mDetail.shortLineVehicleTimeTable}}</p>
                </div>
              </li>
              <li v-if="mDetail.shortLineType==7"><!--高铁-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/高铁.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}——用时{{mDetail.timesStr}}</p>
                  <p>{{mDetail.shortLineVehicleTimeTable}}【{{mDetail.shortLineVehicleNum}}】</p>
                </div>
              </li>
              <li v-if="mDetail.shortLineType==8"><!--地铁-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/地铁.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}——用时{{mDetail.timesStr}}</p>
                  <p style="color:#416367;font-weight:bold;">【{{mDetail.shortLineVehicleNum}}】{{mDetail.shortLineVehicleTimeTable}}</p>
                </div>
              </li>
            </ul>
            <!-- 终点 -->
            <div class="last">
              <img src="../assets/img/icon/9终点.svg" alt="">
              <p>{{mMsg.lineInfoEnd}}</p>
            </div>
          </div>
    		</div>
    	</div>
    </div>
    <div v-else class="noData">
      <img src="../assets/img/没有路线.png" alt="">
      <h1>当前查询路线为空</h1>
    </div>
	  <div class="mobile">
      <!-- <article class="head">想去哪就去哪</article> -->
      <div class="routes" v-for="mMsg,index in msg">
    		<p>方案推荐</p>
    		<div class="tips">
          <div class="detail_info">
            <blockquote style="font-size:15px;display:block">
              起点：{{mMsg.lineInfoStart}}<br/>
              终点：{{mMsg.lineInfoEnd}}<br/>
              <!-- 总时间：{{mMsg.lineInfoTimes}} -￥{{mMsg.lineInfoPrice}} -->
              总时间：{{formatSeconds(mMsg.lineInfoTimes)}}
            </blockquote>
            <ul v-for="mDetail in mMsg.oneCityShortLineList">
              <li v-if="mDetail.shortLineType==1"><!--火车-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/火车.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}——用时{{mDetail.timesStr}}</p>
                  <p>{{mDetail.startTime}}-{{mDetail.endTime}}-{{mDetail.shortLineVehicleNum}}</p>
                </div>
              </li>
              <li v-if="mDetail.shortLineType==2"><!--飞机-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/飞机.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}——用时{{mDetail.timesStr}}</p>
                  <p>{{mDetail.shortLineVehicleTimeTable}}【{{mDetail.shortLineVehicleNum}}】</p>
                </div>
              </li>
              <li v-if="mDetail.shortLineType==3"><!--公交-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/公交.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}—用时{{mDetail.timesStr}}</p>
                  <p style="color:#416367;font-weight:bold;margin:0">【{{mDetail.shortLineVehicleNum}}】{{mDetail.shortLineVehicleTimeTable}}</p>
                </div>
              </li>
              <li v-if="mDetail.shortLineType==4"><!--驾车-->
                <p style="color:#862537;font-weight:bold;">￥{{mDetail.shortLinePrice}}——用时{{mDetail.timesStr}}</p>
                <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                <p>{{mDetail.shortLineVehicleTimeTable}}</p>
              </li>
              <li v-if="mDetail.shortLineType==5"><!--步行-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/步行.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">用时{{mDetail.timesStr}}</p>
                  <p style="color:#416367;font-weight:bold;">{{mDetail.shortLineVehicleInfo}}</p>
                </div>
              </li>
              <li v-if="mDetail.shortLineType==6"><!--大巴-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/大巴.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}——用时{{mDetail.timesStr}}</p>
                  <p style="color:#416367;font-weight:bold;">【{{mDetail.shortLineVehicleNum}}】{{mDetail.shortLineVehicleTimeTable}}</p>
                </div>
              </li>
              <li v-if="mDetail.shortLineType==7"><!--高铁-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/高铁.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}——用时{{mDetail.timesStr}}</p>
                  <p>{{mDetail.shortLineVehicleTimeTable}}【{{mDetail.shortLineVehicleNum}}】</p>
                </div>
              </li>
              <li v-if="mDetail.shortLineType==8"><!--地铁-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/地铁.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}——用时{{mDetail.timesStr}}</p>
                  <p style="color:#416367;font-weight:bold;">【{{mDetail.shortLineVehicleNum}}】{{mDetail.shortLineVehicleTimeTable}}</p>
                </div>
              </li>
            </ul>
            <!-- 终点 -->
            <div class="last">
              <img src="../assets/img/icon/9终点.svg" alt="">
              <p>{{mMsg.lineInfoEnd}}</p>
            </div>
          </div>
    		</div>
    	</div>
    </div>
  </section>
</template>

<script>
import {SERVER} from '@/config';
import Calendar from 'vue-calendar-component';
import BMap from 'BMap';
import TimePicker from '../components/accurateTime/TimePicker';
import '../assets/css/bootstrap.css';
import '../assets/css/bootstrap.min.css';
import '../assets/js/jquery.min.js';
import '../assets/js/popper.min.js';

export default {
  name: 'search_alike',
  components: { Calendar,TimePicker },
  props:['res'],
  data: function(){
    return {
      msg: [],
      flag: true,
      calFlag: false,
      msgDate: '',

      changeHour:'',// 具体时间
      changeMinute:'',
      curHour:'',
      curMinute:'',

      startPoint: '',// 起始坐标
      endPoint: '',// 终点坐标
      city_code: '',//城市id
      city_code2: ''
    }
  },
  created(){
    this.start();
    this.end();
  },
  mounted(){
    let that=this;
    let planStr = sessionStorage.getItem('plan');
    if (planStr=='') {
      that.flag=false;
    }else {
      that.flag = true;
      that.msg = JSON.parse(planStr);
    }
  },
  methods:{
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
    position:function () {
      let that=this;
      let geolocation = new BMap.Geolocation();
      geolocation.getCurrentPosition(function(r){
        if(this.getStatus() == BMAP_STATUS_SUCCESS){
          sessionStorage.setItem("SDKLng",r.point.lng);
          sessionStorage.setItem("SDKLat",r.point.lat);
          $.ajax({
              url:'http://api.map.baidu.com/geocoder/v2/?ak=134db1b9cf1f1f2b4427210932b34dcb&location=' + r.point.lat + ',' + r.point.lng + '&output=json',
              dataType: 'jsonp',
              callback: 'BMap._rd._cbk43398',
              success: function(res) {
                that.city_code=res.result.cityCode;
              },
              error:function(){alert("没找到城市id");}
          });
          $("#icon").css("color","#769164");
          that.startPoint=r.point;
          $("#locate").val("");
        }else {
          alert('failed'+this.getStatus());
        }
      },{enableHighAccuracy: true})//指示浏览器获取高精度的位置，默认false
    },
    position2:function () {
      let that=this;
      let geolocation = new BMap.Geolocation();
      geolocation.getCurrentPosition(function(r){
        if(this.getStatus() == BMAP_STATUS_SUCCESS){
          sessionStorage.setItem("SDKLng",r.point.lng);
          sessionStorage.setItem("SDKLat",r.point.lat);
          $.ajax({
              url:'http://api.map.baidu.com/geocoder/v2/?ak=134db1b9cf1f1f2b4427210932b34dcb&location=' + r.point.lat + ',' + r.point.lng + '&output=json',
              dataType: 'jsonp',
              callback: 'BMap._rd._cbk43398',
              success: function(res) {
                that.city_code2=res.result.cityCode;
              },
              error:function(){alert("没找到城市id");}
          });
          $("#icon2").css("color","#769164");
          that.endPoint=r.point;
          $("#locate2").val("");
        }else {
          alert('failed'+this.getStatus());
        }
      },{enableHighAccuracy: true})//指示浏览器获取高精度的位置，默认false
    },
    start:function(){
      let that=this;
      let map = new BMap.Map("allmap1");
      let ac = new BMap.Autocomplete(
      {
          "input" : "locate",
          "location" : map
      });
      // 点击下拉列表后的事件
      let myValue;
      ac.addEventListener("onconfirm", function(e) {
      	var _value = e.item.value;
        myValue = _value.province +  _value.city +  _value.district +  _value.street +  _value.business;

        // 地址解析
        var myGeo = new BMap.Geocoder();
        myGeo.getPoint(myValue, function(point){
          if (point) {
            that.startPoint=point;
            $.ajax({
                url:'http://api.map.baidu.com/geocoder/v2/?ak=134db1b9cf1f1f2b4427210932b34dcb&location=' + point.lat + ',' + point.lng + '&output=json',
                dataType: 'jsonp',
                callback: 'BMap._rd._cbk43398',
                success: function(res) {
                  that.city_code=res.result.cityCode;
                } ,
                error:function(){alert("没找到城市id");}
            });
          }
        }, "北京");
      });
      $("#icon").css("color","#333");
    },
    end:function(){
      let that=this;
      let map = new BMap.Map("allmap2");
      let ac = new BMap.Autocomplete(
      {
          "input" : "locate2",
          "location" : map
      });
      // 点击下拉列表后的事件
      let myValue;
      ac.addEventListener("onconfirm", function(e) {
      	var _value = e.item.value;
        myValue = _value.province +  _value.city +  _value.district +  _value.street +  _value.business;

        // 地址解析
        var myGeo = new BMap.Geocoder();
        myGeo.getPoint(myValue, function(point){
          if (point) {
            that.endPoint=point;
            $.ajax({
                url:'http://api.map.baidu.com/geocoder/v2/?ak=134db1b9cf1f1f2b4427210932b34dcb&location=' + point.lat + ',' + point.lng + '&output=json',
                dataType: 'jsonp',
                callback: 'BMap._rd._cbk43398',
                success: function(res) {
                  that.city_code2=res.result.cityCode;
                } ,
                error:function(){alert("没找到城市id");}
            });
          }
        }, "北京");
      });
      $("#icon").css("color","#333");
    },
    getCalendar:function(event){//获取日历
      this.calFlag=!this.calFlag;
    },
    clickDay(data){ //选中某天
      let year=data.split('/')[0];
      let month=data.split('/')[1];
      let day=data.split('/')[2];

      if (month<10) {month="0"+month;}
      if (day<10) {day="0"+day;}

      var dataRes=year+"-"+month+"-"+day+" ";
      this.msgDate=dataRes;
    },
    //获取具体时间
    getAccurateTime(){
      if (this.calFlag) {this.calFlag=!this.calFlag;}
    },
    //改变后的changeHour
    hour(data){this.changeHour=data;},
    minute(data){this.changeMinute=data},
    //当前时间
    timeHour(data){this.curHour=data},
    timeMinute(data){this.curMinute=data},
    // 查询
    search:function(){
      let that=this;
      let code=this.city_code;
      let code2=this.city_code2;

      let a=this.startPoint;
      let aLng=a.lng;
      let aLat=a.lat;
      let aa=aLng+","+aLat;

      let b=this.endPoint;
      let bLng=b.lng;
      let bLat=b.lat;
      let bb=bLng+","+bLat;

      let locate=$("#locate").val();
      let locate2=$("#locate2").val();
      let c=$('#time').val();

      //精确时间
      let accurateTime=this.curHour+":"+this.curMinute+":"+"00";
      let accurateTime2=this.changeHour+":"+this.changeMinute+":"+"00";
      let q;
      if (this.changeHour=='' && this.changeMinute=='') {q=accurateTime;}
      else if (this.changeHour=='') {q=this.curHour+":"+this.changeMinute+":"+"00";}
      else if (this.changeMinute=='') {q=this.changeHour+":"+this.curMinute+":"+"00";}
      else {q=accurateTime2;}
      let cc=c+""+q;

      // console.log(code);
      // console.log(code2);
      // console.log(aa);
      // console.log(bb);
      // console.log(cc);
      // console.log($("#locate").val());
      // console.log($("#locate2").val());

      if(a==""){$("#locate").focus();}
      else if (b=="") {$("#locate2").focus();}
      else if (c=="") {$("#time").focus();}
      else if (a=="" || c=="") {$("#locate").focus();}
      else if (a==""||b=="") {$("#locate").focus();}
      else if (b=="" || c=="") {$("#locate2").focus();}
      else if (code!=code2) {
        $(".loading").css("display","block");
        $(".btn").css("display","none");
        // 不同城市
        this.axios({
          method: 'post',
          url: 'http://192.168.43.159:65525/otherCity.line',
          headers: {'Content-Type': 'application/x-www-form-urlencoded'},
          data: {
            endCid: code2,
            endPoint: bb,
            startCid: code,
            startPoint: aa,
            startTime: c+""+q,
            tripTypeList: ''
          }
        }).then(function (res) {
          sessionStorage.setItem('plan',JSON.stringify(res.data.lineInfoList));
          that.$router.push({path:'/search_alien',});
          $(".loading").css("display","none");
          $(".btn").css("display","block");
        }).catch(function (err) {
          console.log(err);
          $(".loading").css("display","none");
          $(".btn").css("display","block");
        });
      }else if (code==code2) {
        $(".loading").css("display","block");
        $(".btn").css("display","none");
        // 相同城市
        this.axios({
          method: 'post',
          url: 'http://192.168.43.159:65526/oneCity.line',
          data: {
            cId: code,
            end: $("#locate2").val(),
            endPoint: bb,
            start: $("#locate").val(),
            startDate: cc,
            startPoint: aa,
            travelScene: ''
          },
          headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        }).then(function (res) {
          if(res.data.code == 0){
            alert(data.msg);
          }else if (res.data.code == -1) {
            alert("系统繁忙，请稍后再试");
            $(".loading").css("display","none");
            $(".btn").css("display","block");
          }else if(res.data.code == 1){
            that.flag=false;
            sessionStorage.setItem('plan',JSON.stringify(res.data.oneCityLineList));
            that.$router.push({
              path:'/search_alike',
            });
            that.flag=true;
            $(".loading").css("display","none");
            $(".btn").css("display","block");
          }
        }).catch(function (err) {
          console.log(err);
          $(".loading").css("display","none");
          $(".btn").css("display","block");
        });
      }
    },
  }
}
</script>

<style lang="css" scoped>
/*pc端*/
@media screen and (min-width: 768px){
  .mobile{display: none;}
  .pc{
    padding-top: 100px;
    padding-bottom: 85px;
    background: url('../assets/img/bg-pc.jpg');
    background-repeat: no-repeat;
    background-size: cover;
    background-attachment: fixed;
  }
	a:hover,a:focus{
		text-decoration: none;
	}
  li{float: left;list-style: none;}
  .search_box{
    width: 80%;
    padding: 20px;
		background: #eef1f8;
		border: 1px solid #769164;
		border-radius: 4px;
    margin: 0 auto 20px;
	}
  .best{
    width: 170px;
    height: 170px;
    overflow: hidden;
    position: absolute;
    top: 80px;
    right: 20px;
    /* background: url("../assets/img/best.png") no-repeat; */
    background-size: cover;
  }
  .input-group{
    padding:0 20px;
    margin: auto;
  }
  .form-control{background: #fff;}
  .calendar{
    position: absolute;
    z-index: 9999;
    top: 40px;
    left: 0;
  }
  .buju{
    height: 35px;
    position: relative;
  }
  .btn{
    width: 80%;
    background-color: #769164;
    text-align: center;
    font-size: 14px;
    border-radius: 4px;
    color: #fff;
  }
  .btn:hover{color: #fff;}
	/* 路线方案 */
	.routes{
    width: 80%;
    margin: 0 auto;
	}
	.routes>p{
    /* margin: 10px 0px 0px; */
    color: #eee;
    font-size: 16px;
	}
  .tips:hover .detail_info{
    /* box-shadow: 10px 10px 5px #888888; */
    box-shadow: darkgrey 10px 10px 30px 5px;
  }
	.tips{
		padding:20px;
		background: #eef1f8;
		margin-top: 10px;
		border: 1px solid #769164;
		border-radius: 10px;
		display: flex;
		flex-wrap: wrap;
	}
  .detail_info{
		width: 100%;
		padding: 10px;
    border-radius: 4px;
		color: #000;
		background: #fff;
		display: flex;
		flex-wrap: wrap;
	}
	.detail_info span{
    line-height: 50px;
    font-size: 14px;
	}
  /* 图标+地点信息——线 */
  ul{
    height: 90px;
    padding: 10px;
  }
  .box{
    float: left;
  }
	ul>li,.last{
		height: 100%;
		text-align: center;
    padding: 2px;
	}
	li img,.last>img{
		width: 30px;
		height: 30px;
	}
	li>p{
    margin: 4px 0 2px;
    color: #555;
    font-size: 14px;
  }
}
/*手机端*/
@media screen and (max-width: 767px){
  li{list-style: none;}
 .pc{display: none;}
 .mobile{display: block;}
 .head{
   width: 100%;
   position: fixed;
   text-align: center;
   background: #769164;
   color: #fff;
   font-weight: bold;
   font-size: 17px;
   line-height: 54px;
   margin-bottom: 30px;
 }
 .best{
   width: 90px;
   height: 90px;
   overflow: hidden;
   position: absolute;
   top: 50px;
   right: 20px;
   /* background: url("../assets/img/best.png") no-repeat; */
   background-size: cover;
 }
 /* 路线方案 */
 .routes{
   width: 90%;
   margin: 0 auto;
 }
 .routes>p{margin: 20px 0px 0px;}
 .tips{
   padding:10px;
   margin-top: 10px;
   background: #eef1f8;
   border: 1px solid #769164;
   border-radius: 10px;
   display: flex;
   flex-wrap: wrap;
 }
 .routes:nth-child(1)>.tips{
   background: #769164;
 }
 .detail_info{
   width: 100%;
   padding: 10px;
   border-radius: 4px;
   color: #000;
   background: #fff;
   display: flex;
   flex-wrap: wrap;
 }
 .detail_info span{
   line-height: 50px;
   font-size: 12px;
 }
 .detail_info>ul{
   height: 90px;
   padding: 10px;
   display: block;
 }
 .box{float: left;}
 ul>li,.last{
   text-decoration: none;
   text-align: center;
   padding: 2px;
 }
 li img,.last>img{
   width: 30px;
   height: 30px;
 }
 li p{
   margin: 0;
   color: #555;
   font-size: 14px;
 }
}
</style>
