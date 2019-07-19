<template lang="html">
  <div>
    <section id="pc">
  		<div class="jumbotron">
        <transition-group tag='ul' name='img'>
			    <li v-for='(image,index) in imgs' :key="'info-'+index" v-show='index===mark'>
						<div class="divImg" :style="{backgroundImage: 'url('+image+')'}"></div>
			    </li>
				</transition-group>
      </div>
  		<div class="panel panel-default">
  		  <div class="panel-heading">
  		    <p class="panel-title">想去哪就去哪~</p>
  		  </div>
  		  <div class="panel-body">
          <div id="allmap1" v-show="mapview" class="allmap allmap1"></div>
          <div id="allmap2" v-show="mapview2" class="allmap allmap2"></div>
  				<article class="site">
            <!-- <div class="change"><a href="#" @click="changeSite">换</a></div> -->
            <div class="form-item">
              <label>出发地</label>
    					<div class="input-group input-group-sm">
                <div @click="get_start">
                  <input type="text" id="locate" class="form-control" style="height:30px;font-size:12px;border-top-left-radius:3px;border-bottom-left-radius:3px;" placeholder="出发地"/>
                </div>
                <span class="input-group-addon" @click="getMap">
                  <span id="pc_icon" class="glyphicon glyphicon-map-marker" aria-hidden="true"></span>
                </span>
    					</div>
            </div>
            <div class="form-item">
              <label>到达地</label>
    					<div class="input-group input-group-sm">
                <div @click="get_end">
                  <input type="text" id="locate2" class="form-control" style="height:30px;font-size:12px;border-top-left-radius:3px;border-bottom-left-radius:3px;" placeholder="目的地"/>
                </div>
                <span class="input-group-addon"> <!-- @click="getMap2"-->
                  <span id="pc_icon2" class="glyphicon glyphicon-map-marker" aria-hidden="true"></span>
                </span>
    					</div>
            </div>
  				</article>
  				<article class="time">
            <div class="form-item">
              <label>出发日期</label>
    					<div class="input-group input-group-sm" @click="getCalendar">
                <input readonly="readonly" type="text" id="time" v-model="calendar_data" class="form-control" placeholder="yyyy-mm-dd">
    						<span class="input-group-addon"><span class="glyphicon glyphicon-calendar" aria-hidden="true"></span></span>
    					</div>
              <Calendar class="calendar" v-show="calFlag"
                  v-on:choseDay="clickDay"
                  :sundayStart="true"
              ></Calendar>
            </div>
  				</article>
          <article class="accurateTime" @click="getAccurateTime">
            <label>出发时间</label>
            <TimePicker v-on:hour="hour" v-on:minute="minute" v-on:timeHour="timeHour" v-on:timeMinute="timeMinute"/>
          </article>
  				<article class="search" @click="search">
            <img id="loading" class="loading" src="../assets/img/icon/loading.gif" alt="加载中……">
            <div class="btn">查询</div>
  				</article>
  		  </div>
  		</div>
  	</section>
  	<section id="phone">
      <article class="head">想去哪就去哪</article>
      <article class="site">
        <div class="form-item">
          <div class="input-group input-group-sm">
            <input type="text" id="phone_locate" @click="start" class="form-control" placeholder="你的位置">
            <span class="input-group-addon" @click="phone_position">
              <span class="glyphicon glyphicon-map-marker" id="phone_icon" aria-hidden="true"></span>
            </span>
          </div>
        </div>
        <div class="form-item">
          <div class="input-group input-group-sm">
            <input type="text" id="phone_locate2" @click="end" class="form-control" placeholder="你要去哪">
            <span class="input-group-addon" @click="phone_position2">
              <span class="glyphicon glyphicon-map-marker" id="phone_icon2" aria-hidden="true"></span>
            </span>
          </div>
        </div>
      </article>
      <article class="time">
        <div class="form-item">
          <div class="input-group input-group-sm">
            <input type="text" id="phone_time" @click="phone_calendar" v-model="calendarMsg" class="form-control" placeholder="日期">
          </div>
        </div>
        <div class="phone_calendar" v-show="calendarShow">
          <Calendar
              v-on:choseDay="phone_clickDay"
              :sundayStart="true"
          ></Calendar>
        </div>
  		</article>
      <article class="accurateTime">
        <TimePicker v-on:hour="hour" v-on:minute="minute" v-on:timeHour="timeHour" v-on:timeMinute="timeMinute"/>
      </article>
  		<article class="search" @click="phone_search">
        <img id="loading" class="loading" src="../assets/img/icon/loading.gif" alt="加载中……">
  			<router-link to="" class="btn">查询</router-link>
  		</article>
  	</section>
  </div>
</template>

<script>
import {SERVER} from '@/config';
import Calendar from 'vue-calendar-component';
import BMap from 'BMap';
import imgIcon from '../assets/img/icon/map_icon.png';
import TimePicker from '../components/accurateTime/TimePicker'
import bgImg from '../assets/img/bg.jpg';
import bgImg2 from '../assets/img/bg2.jpg';
import bgImg3 from '../assets/img/bg3.jpg';
import bgImg4 from '../assets/img/bg4.jpg';
import bgImg5 from '../assets/img/bg5.jpg';
import bgImg6 from '../assets/img/bg6.jpg';

export default {
  name: 'index',
  components: { Calendar,TimePicker },
  data: function(){
    return {
      mark:0,
      imgs:[bgImg, bgImg2, bgImg3, bgImg4, bgImg5, bgImg6],
			loginImgStyle: {
				backgroundPosition: '0px 0px',
				backgroundSize: 'cover',
				backgroundRepeat: 'no-repeat',
				backgroundImage: bgImg,
			},

      mapview:false,
      mapview2:false,
      calFlag:false,

      calendar_data:'',// 日历时间
      changeHour:'',// 具体时间
      changeMinute:'',
      curHour:'',
      curMinute:'',

      startPoint: '',// 起始坐标
      endPoint: '',// 终点坐标
      city_code: '',//城市id
      city_code2: '',

      //phone
      calendarShow: false,
      calendarMsg: ''
    }
  },
  created(){
    this.play();
  },
  methods: {
    // 轮播
    autoPlay() {
			if(this.mark<this.imgs.length-1){
				this.mark++;
			}else{
				this.mark = 0;
			}
		},
		play() {
	    setInterval(this.autoPlay, 5000)
		},
    //定位
    getMap(){
      if (this.mapview2) {
        this.mapview2=!this.mapview2;
      }else if (this.calFlag) {
        this.calFlag=!this.calFlag;
      }
      this.mapview=!this.mapview;
    },
    // getMap2(){
    //   if (this.mapview) {
    //     this.mapview=!this.mapview;
    //   }else if (this.calFlag) {
    //     this.calFlag=!this.calFlag;
    //   }
    //   this.mapview2=!this.mapview2;
    // },
    get_start(){
      if (this.mapview2) {this.mapview2=!this.mapview2;}
      else if (this.calFlag) {this.calFlag=!this.calFlag;}
      this.mapview=true;

      // 获取当前坐标
      let geolocation = new BMap.Geolocation();
      let that=this;
      geolocation.getCurrentPosition(function(r){
        if(this.getStatus() == BMAP_STATUS_SUCCESS){
          // 搜索具体地点信息
          $.ajax({
              url:'http://api.map.baidu.com/geocoder/v2/?ak=134db1b9cf1f1f2b4427210932b34dcb&callback=renderReverse&callback=renderReverse&location=' + r.point.lat + ',' + r.point.lng + '&output=json&pois=1',
              dataType: 'jsonp',
              success: function(res) {
                if (res.result.poiRegions==""||res.result.poiRegions==null) {
                  var result=res.result.formatted_address+res.result.sematic_description;
                }else {
                  var result=res.result.formatted_address+res.result.poiRegions[0].name;
                }
                $('#locate').val(result);
              },
              error:function(){alert("没找到城市");}
          });
          // 搜索城市id
          $.ajax({
              url:'http://api.map.baidu.com/geocoder/v2/?ak=134db1b9cf1f1f2b4427210932b34dcb&location=' + r.point.lat + ',' + r.point.lng + '&output=json',
              dataType: 'jsonp',
              callback: 'BMap._rd._cbk43398',
              success: function(res) {
                that.city_code=res.result.cityCode;
              },
              error:function(){alert("没找到城市");}
          });
          // 创建地图
          let map = new BMap.Map("allmap1");
          let point = new BMap.Point(r.point);
          let icon = new BMap.Icon(imgIcon,new BMap.Size(20,22));
          map.centerAndZoom(r.point,15);
          map.enableScrollWheelZoom(true);//开启滚动

          that.startPoint=r.point;
          var mk = new BMap.Marker(r.point);
          map.addOverlay(mk);
          map.panTo(r.point);
          $("#pc_icon").css("color","#769164");
          // 地图点击事件
          map.addEventListener('click', function (e) {
            // 搜索详细地址信息
            $.ajax({
                url:'http://api.map.baidu.com/geocoder/v2/?ak=134db1b9cf1f1f2b4427210932b34dcb&callback=renderReverse&callback=renderReverse&location=' + e.point.lat + ',' + e.point.lng + '&output=json&pois=1',
                dataType: 'jsonp',
                success: function(res) {
                  if (res.result.poiRegions==""||res.result.poiRegions==null) {
                    var result=res.result.formatted_address+res.result.sematic_description;
                  }else {
                    var result=res.result.formatted_address+res.result.poiRegions[0].name;
                  }
                  $('#locate').val(result);
                },
                error:function(){alert("没找到城市");}
            });
            // 搜索城市id
            $.ajax({
                url:'http://api.map.baidu.com/geocoder/v2/?ak=134db1b9cf1f1f2b4427210932b34dcb&location=' + e.point.lat + ',' + e.point.lng + '&output=json',
                dataType: 'jsonp',
                callback: 'BMap._rd._cbk43398',
                success: function(res) {
                  that.city_code=res.result.cityCode;
                } ,
                error:function(){alert("没找到城市id");}
            });
            map.removeOverlay(mk);
            mk = new BMap.Marker(e.point,{icon:icon});
            map.addOverlay(mk);
            that.startPoint=e.point;
          });
          //建立一个自动完成的对象
          let ac = new BMap.Autocomplete({
              "input" : "locate",
              "location" : map
          });
          // 鼠标点击下拉列表后的事件
          ac.addEventListener("onconfirm", function(e) {
            let myValue;
          	var _value = e.item.value;
            myValue = _value.province +  _value.city +  _value.district +  _value.street +  _value.business;
            // 地址解析
            var myGeo = new BMap.Geocoder();
            myGeo.getPoint(myValue, function(point){
              if (point) {
                // 获取城市id
                $.ajax({
                    url:'http://api.map.baidu.com/geocoder/v2/?ak=134db1b9cf1f1f2b4427210932b34dcb&location=' + point.lat + ',' + point.lng + '&output=json',
                    dataType: 'jsonp',
                    callback: 'BMap._rd._cbk43398',
                    success: function(res) {
                      that.city_code=res.result.cityCode;
                    } ,
                    error:function(){alert("没找到城市id");}
                });
                that.startPoint=point;
                map.centerAndZoom(point, 15);
                map.removeOverlay(mk);
                mk = new BMap.Marker(point,{icon:icon});
                map.addOverlay(mk);
              }
            }, "");
          });
        }
        else {alert('failed'+this.getStatus());}
      });
    },
    get_end(){
      if (this.mapview) {this.mapview=!this.mapview;}
      else if (this.calFlag) {this.calFlag=!this.calFlag;}
      // this.mapview2=true;

      // 获取当前坐标
      let geolocation = new BMap.Geolocation();
      let that=this;
      geolocation.getCurrentPosition(function(r){
        if(this.getStatus() == BMAP_STATUS_SUCCESS){
          // 搜索具体地点信息
          $.ajax({
              url:'http://api.map.baidu.com/geocoder/v2/?ak=134db1b9cf1f1f2b4427210932b34dcb&callback=renderReverse&callback=renderReverse&location=' + r.point.lat + ',' + r.point.lng + '&output=json&pois=1',
              dataType: 'jsonp',
              success: function(res) {
                if (res.result.poiRegions==""||res.result.poiRegions==null) {
                  var result=res.result.formatted_address+res.result.sematic_description;
                }else {
                  var result=res.result.formatted_address+res.result.poiRegions[0].name;
                }
                // $('#locate2').val(result);
              },
              error:function(){alert("没找到城市");}
          });
          // 搜索城市id
          $.ajax({
              url:'http://api.map.baidu.com/geocoder/v2/?ak=134db1b9cf1f1f2b4427210932b34dcb&location=' + r.point.lat + ',' + r.point.lng + '&output=json',
              dataType: 'jsonp',
              callback: 'BMap._rd._cbk43398',
              success: function(res) {
                that.city_code2=res.result.cityCode;
              },
              error:function(){alert("没找到城市");}
          });
          // 创建地图
          let map = new BMap.Map("allmap2");
          let point = new BMap.Point(r.point);
          let icon = new BMap.Icon(imgIcon,new BMap.Size(20,22));
          map.centerAndZoom(r.point,15);
          map.enableScrollWheelZoom(true);//开启滚动

          that.endPoint=r.point;
          var mk = new BMap.Marker(r.point);
          map.addOverlay(mk);
          map.panTo(r.point);
          $("#pc_icon2").css("color","#769164");
          // 地图点击事件
          map.addEventListener('click', function (e) {
            // 搜索详细地址信息
            $.ajax({
                url:'http://api.map.baidu.com/geocoder/v2/?ak=134db1b9cf1f1f2b4427210932b34dcb&callback=renderReverse&callback=renderReverse&location=' + e.point.lat + ',' + e.point.lng + '&output=json&pois=1',
                dataType: 'jsonp',
                success: function(res) {
                  if (res.result.poiRegions==""||res.result.poiRegions==null) {
                    var result=res.result.formatted_address+res.result.sematic_description;
                  }else {
                    var result=res.result.formatted_address+res.result.poiRegions[0].name;
                  }
                  $('#locate2').val(result);
                },
                error:function(){alert("没找到城市");}
            });
            // 搜索城市id
            $.ajax({
                url:'http://api.map.baidu.com/geocoder/v2/?ak=134db1b9cf1f1f2b4427210932b34dcb&location=' + e.point.lat + ',' + e.point.lng + '&output=json',
                dataType: 'jsonp',
                callback: 'BMap._rd._cbk43398',
                success: function(res) {
                  that.city_code2=res.result.cityCode;
                } ,
                error:function(){alert("没找到城市id");}
            });
            map.removeOverlay(mk);
            mk = new BMap.Marker(e.point,{icon:icon});
            map.addOverlay(mk);
            that.endPoint=e.point;
          });
          //建立一个自动完成的对象
          let ac = new BMap.Autocomplete({
              "input" : "locate2",
              "location" : map
          });
          // 鼠标点击下拉列表后的事件
          ac.addEventListener("onconfirm", function(e) {
            let myValue;
          	var _value = e.item.value;
            myValue = _value.province +  _value.city +  _value.district +  _value.street +  _value.business;
            // 地址解析
            var myGeo = new BMap.Geocoder();
            myGeo.getPoint(myValue, function(point){
              if (point) {
                // 获取城市id
                $.ajax({
                    url:'http://api.map.baidu.com/geocoder/v2/?ak=134db1b9cf1f1f2b4427210932b34dcb&location=' + point.lat + ',' + point.lng + '&output=json',
                    dataType: 'jsonp',
                    callback: 'BMap._rd._cbk43398',
                    success: function(res) {
                      that.city_code2=res.result.cityCode;
                    },
                    error:function(){alert("没找到城市id");}
                });
                that.endPoint=point;
                map.centerAndZoom(point, 15);
                map.removeOverlay(mk);
                mk = new BMap.Marker(point,{icon:icon});
                map.addOverlay(mk);
              }
            }, "");
          });
        }
        else {alert('failed'+this.getStatus());}
      });
    },
    //交换 起始点
    changeSite: function(){let change;},
    getCalendar:function(event){//获取日历
      if (this.mapview) {
        this.mapview=!this.mapview;
      }else if (this.mapview2) {
        this.mapview2=!this.mapview2;
      }
      this.calFlag=!this.calFlag;
    },
    clickDay(data){ //选中某天
      let year=data.split('/')[0];
      let month=data.split('/')[1];
      let day=data.split('/')[2];

      if (month<10) {month="0"+month;}
      if (day<10) {day="0"+day;}

      var dataRes=year+"-"+month+"-"+day+" ";
      this.calendar_data=dataRes;
      this.calFlag=!this.calFlag;
    },
    //获取具体时间
    getAccurateTime(){
      if (this.mapview) {
        this.mapview=!this.mapview;
      }else if (this.mapview2) {
        this.mapview2=!this.mapview2;
      }else if (this.calFlag) {
        this.calFlag=!this.calFlag;
      }
    },
    //改变后的changeHour
    hour(data){this.changeHour=data;},
    minute(data){this.changeMinute=data},
    //当前时间
    timeHour(data){this.curHour=data},
    timeMinute(data){this.curMinute=data},
    //查找
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
      if (this.changeHour=="" && this.changeMinute=="") {q=accurateTime;}
      else if (this.changeHour=="" && this.changeMinute!="") {q=this.curHour+":"+this.changeMinute+":"+"00";}
      else if (this.changeHour!="" && this.changeMinute=="") {q=this.changeHour+":"+this.curMinute+":"+"00";}

      else if (this.changeHour==0 && this.changeMinute==0) {console.log("ssssssssss");q="00"+":"+"00"+":"+"00";}
      else if (this.changeHour==0 && this.changeMinute=="") {q="00"+":"+this.curMinute+":"+"00";}
      else if (this.changeHour==0 && this.changeMinute!="") {q="00"+":"+this.changeMinute+":"+"00";}

      else if (this.changeHour=="" && this.changeMinute==0) {q=this.curHour+":"+"00"+":"+"00";}
      else if (this.changeHour!="" && this.changeMinute==0) {q=this.changeHour+":"+"00"+":"+"00";}

      else {q=accurateTime2;}
      let cc=c+""+q;

      // console.log(code);
      // console.log(code2);
      // console.log(aa);
      // console.log(bb);
      // console.log($("#locate").val());
      // console.log($("#locate2").val());
      // console.log(cc);

      if(a==""){$("#locate").focus();}
      else if (b=="") {$("#locate2").focus();}
      else if (c=="") {$("#time").focus();}
      else if (a=="" || c=="") {$("#locate").focus();}
      else if (a==""||b=="") {$("#locate").focus();}
      else if (b=="" || c=="") {$("#locate2").focus();}
      else if (code!=code2) {
        $(".loading").css("display","block");
        $(".btn").css("background","#fff");
        // 不同城市
        this.axios({
          method: 'post',
          url: 'http://192.168.1.101:65525/otherCity.line',
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
          if (res.data.code==-1) {
            alert("系统繁忙，请稍后再试");
            that.$router.push({path:'/search_alien',});
            $(".loading").css("display","none");
            $(".btn").css("background","#769164");
          }else if (res.data.code==0) {
            alert(data.msg);
            that.$router.push({path:'/search_alien',});
            $(".loading").css("display","none");
            $(".btn").css("background","#769164");
          }else if (res.data.code==1) {
            sessionStorage.setItem('plan',JSON.stringify(res.data));
            that.$router.push({path:'/search_alien',});
            $(".loading").css("display","none");
            $(".btn").css("background","#769164");
          }
        }).catch(function (err) {
          console.log(err);
          $(".loading").css("display","none");
          $(".btn").css("background","#769164");
        });
      }else if (code==code2) {
        $(".loading").css("display","block");
        $(".btn").css("background","#fff");
        // 相同城市
        this.axios({
          method: 'post',
          url: 'http://192.168.1.101:65526/oneCity.line',
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
            $(".btn").css("background","#769164");
          }else if(res.data.code == 1){
            sessionStorage.setItem('plan',JSON.stringify(res.data.oneCityLineList));
            that.$router.push({path:'/search_alike'});
            $(".loading").css("display","none");
            $(".btn").css("background","#769164");
          }
        }).catch(function (err) {
          console.log(err);
          $(".loading").css("display","none");
          $(".btn").css("background","#769164");
        });
      }
    },

    // 手机端页面事件
    // 定位
    phone_position:function () {
      let that=this;
      let geolocation = new BMap.Geolocation();
      geolocation.getCurrentPosition(function(r){
        if(this.getStatus() == BMAP_STATUS_SUCCESS){
          $.ajax({
              url:'http://api.map.baidu.com/geocoder/v2/?ak=134db1b9cf1f1f2b4427210932b34dcb&location=' + r.point.lat + ',' + r.point.lng + '&output=json',
              dataType: 'jsonp',
              callback: 'BMap._rd._cbk43398',
              success: function(res) {
                that.city_code=res.result.cityCode;
              },
              error:function(){alert("没找到城市id");}
          });
          $("#phone_icon").css("color","#769164");
          that.startPoint=r.point;
          $("#phone_locate").val("");
        }else {
          alert('failed'+this.getStatus());
        }
      },{enableHighAccuracy: true})//指示浏览器获取高精度的位置，默认false
    },
    phone_position2:function () {
      let that=this;
      let geolocation = new BMap.Geolocation();
      geolocation.getCurrentPosition(function(r){
        if(this.getStatus() == BMAP_STATUS_SUCCESS){
          $.ajax({
              url:'http://api.map.baidu.com/geocoder/v2/?ak=134db1b9cf1f1f2b4427210932b34dcb&location=' + r.point.lat + ',' + r.point.lng + '&output=json',
              dataType: 'jsonp',
              callback: 'BMap._rd._cbk43398',
              success: function(res) {
                that.city_code2=res.result.cityCode;
              },
              error:function(){alert("没找到城市id");}
          });
          $("#phone_icon2").css("color","#769164");
          that.endPoint=r.point;
          $("#phone_locate2").val("");
        }else {
          alert('failed'+this.getStatus());
        }
      },{enableHighAccuracy: true})//指示浏览器获取高精度的位置，默认false
    },
    // 键盘事件
    start(){},
    end(){},
    // start:function(){
    //   // 获取当前坐标
    //   let geolocation = new BMap.Geolocation();
    //   let that=this;
    //   geolocation.getCurrentPosition(function(r){
    //     if(this.getStatus() == BMAP_STATUS_SUCCESS){
    //       that.startPoint=r.point;
    //       let map = new BMap.Map("allmap1");
    //       let point = new BMap.Point(r.point);
    //       map.centerAndZoom(r.point,15);
    //       let ac = new BMap.Autocomplete({
    //           "input" : "phone_locate",
    //           "location" : map
    //       });
    //       ac.addEventListener("onconfirm", function(e) {
    //         let myValue;
    //       	var _value = e.item.value;
    //         myValue = _value.province +  _value.city +  _value.district +  _value.street +  _value.business;
    //         // 地址解析
    //         var myGeo = new BMap.Geocoder();
    //         myGeo.getPoint(myValue, function(point){
    //           if (point) {
    //             // 获取城市id
    //             $.ajax({
    //                 url:'http://api.map.baidu.com/geocoder/v2/?ak=134db1b9cf1f1f2b4427210932b34dcb&location=' + point.lat + ',' + point.lng + '&output=json',
    //                 dataType: 'jsonp',
    //                 callback: 'BMap._rd._cbk43398',
    //                 success: function(res) {
    //                   that.city_code=res.result.cityCode;
    //                 } ,
    //                 error:function(){alert("没找到城市id");}
    //             });
    //             that.startPoint=point;
    //             map.centerAndZoom(point, 15);
    //             map.addOverlay(new BMap.Marker(point));
    //           }
    //         }, "");
    //       });
    //     }
    //     else {alert('failed'+this.getStatus());}
    //   });
    // },
    // end:function(){
    //   // 获取当前坐标
    //   let geolocation = new BMap.Geolocation();
    //   let that=this;
    //   geolocation.getCurrentPosition(function(r){
    //     if(this.getStatus() == BMAP_STATUS_SUCCESS){
    //       that.endPoint=r.point;
    //       let map = new BMap.Map("allmap2");
    //       let point = new BMap.Point(r.point);
    //       map.centerAndZoom(r.point,15);
    //       let ac = new BMap.Autocomplete({
    //           "input" : "phone_locate2",
    //           "location" : map
    //       });
    //       ac.addEventListener("onconfirm", function(e) {
    //         let myValue;
    //       	var _value = e.item.value;
    //         myValue = _value.province +  _value.city +  _value.district +  _value.street +  _value.business;
    //         // 地址解析
    //         var myGeo = new BMap.Geocoder();
    //         myGeo.getPoint(myValue, function(point){
    //           if (point) {
    //             // 获取城市id
    //             $.ajax({
    //                 url:'http://api.map.baidu.com/geocoder/v2/?ak=134db1b9cf1f1f2b4427210932b34dcb&location=' + point.lat + ',' + point.lng + '&output=json',
    //                 dataType: 'jsonp',
    //                 callback: 'BMap._rd._cbk43398',
    //                 success: function(res) {
    //                   that.city_code2=res.result.cityCode;
    //                 } ,
    //                 error:function(){alert("没找到城市id");}
    //             });
    //             that.endPoint=point;
    //             map.centerAndZoom(point, 15);
    //             map.addOverlay(new BMap.Marker(point));
    //           }
    //         }, "");
    //       });
    //     }
    //     else {alert('failed'+this.getStatus());}
    //   });
    // },

    // 日历
    phone_calendar:function(){
      this.calendarShow=!this.calendarShow;
      // $(".phone_calendar").css("display","block");
    },
    phone_clickDay(data){ //选中某天
      let year=data.split('/')[0];
      let month=data.split('/')[1];
      let day=data.split('/')[2];

      if (month<10) {month="0"+month;}
      if (day<10) {day="0"+day;}

      var dataRes=year+"-"+month+"-"+day+" ";
      this.calendarMsg=dataRes;
      $(".phone_calendar").css("display","none");
    },
    // 查找
    phone_search:function(){
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

      let locate=$("#phone_locate").val();
      let locate2=$("#phone_locate2").val();
      let c=$('#phone_time').val();

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
      // console.log($("#phone_locate").val());
      // console.log($("#phone_locate2").val());

      if(a==""){$("#phone_locate").focus();}
      else if (b=="") {$("#phone_locate2").focus();}
      else if (c=="") {$("#time").focus();}
      else if (a=="" || c=="") {$("#phone_locate").focus();}
      else if (a==""||b=="") {$("#phone_locate").focus();}
      else if (b=="" || c=="") {$("#phone_locate2").focus();}
      else if (code!=code2) {
        $(".loading").css("display","block");
        $(".btn").css("background","#fff");
        // 不同城市
        this.axios({
          method: 'post',
          url: 'http://192.168.1.101:65525/otherCity.line',
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
          $(".btn").css("background","#769164");
        }).catch(function (err) {
          console.log(err);
          $(".loading").css("display","none");
          $(".btn").css("background","#769164");
        });
      }else if (code==code2) {
        $(".loading").css("display","block");
        $(".btn").css("background","#769164");
        // 相同城市
        this.axios({
          method: 'post',
          url: 'http://192.168.1.101:65526/oneCity.line',
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
            $(".btn").css("background","#769164");
          }else if(res.data.code == 1){
            sessionStorage.setItem('plan',JSON.stringify(res.data.oneCityLineList));
            that.$router.push({path:'/search_alike'});
            $(".loading").css("display","none");
            $(".btn").css("background","#769164");
          }
        }).catch(function (err) {
          console.log(err);
          $(".loading").css("display","none");
          $(".btn").css("background","#769164");
        });
      }
    }
  }
}
</script>

<style lang="css" scoped>
/*pc端*/
@media screen and (min-width: 768px){
  /* 下拉框 */
  .search_cities{
    padding: 0 12px;
    width: 99%;
    position: absolute;
    left: 0;
    z-index: 9999;
    background: #fff;
    box-shadow: 1px 2px 1px rgba(0,0,0,.15);
    border-radius: 0 0 2px 2px;
  }
  .search_cities_a{top: 30px;}
  .search_cities_b{top: 30px;}
  .search_cities li{
    list-style: none;
    cursor: pointer;
    border-radius: 2px;
    height: 26px;
    line-height: 26px;
    overflow: hidden;
  }
  .choice_cities li:hover, .search_cities li:hover, .gray{background: #ccc;}
  #phone{display: none;}
  #pc{
    height: 100vh;
    position: relative;
  }
  #pc .jumbotron{
    width: 100vw;
    height: 100vh;
    margin: 0;
    padding: 0;
    overflow: hidden;
    position: relative;
  }
  .jumbotron ul li{width: 100%;height: 100%;position: absolute;}
  .jumbotron .divImg {
  		background-position: 0px;
  		background-size: cover;
  		background-repeat: no-repeat;
  		width: 100%;height: 100%;
	 }
  .img-enter-active,.img-leave-active {transition: all 4s;}
	.img-enter,.img-leave-to {opacity: 0;}
	.img-enter-to,.img-leave {opacity: 1;}
  #bgImgs{
    max-width: 100%;
    max-height: 100%;
  }
  .switch span{
    position: absolute;
    width: 50px;
    height: 50px;
    line-height: 50px;
    text-align: center;
    background-color: rgba(0,0,0,.1);
    font-size: 20px;
    color: #ffffff;
    top: 50%;
    margin-top: -25px;
    cursor: pointer;
    font-family: "宋体";
  }
  .switch span:hover{
    background-color: rgba(0,0,0,.5);
  }
  .prev{left: 0;}
  .next{right: 0;}
  #pc .panel{
    width: 510px;
    position: absolute;
    left: 10%;
    top: 20%;
    background: #fff;
    border-radius: 4px;
  }
  /* 居中 */
  #pc .panel-body{
    padding: 16px 48px 38px;
  }
  #pc .panel-heading{
    background: #769164;
    height: 46px;
    padding: 10px 15px;
    color: #F8F8FF;
    border-radius: 4px;
  }
  .form-item{margin-top: 16px;}
  article span{
    text-align: center;
    color: #000;
  }
  .change{
    position: absolute;
    top: 89px;
    right: 56px;
    width: 24px;
    height: 60px;
    border: 1px solid #DEDEDE;
    border-left: none;
    cursor: pointer;
  }
  .change > a{
    position: absolute;
    top: 18px;
    right: -13px;
    display: inline-block;
    border-radius: 50%;
    background: #DEDEDE;
    color: white;
    width: 25px;
    height: 25px;
    font-size: 14px;
    line-height: 25px;
    text-align: center;
  }
  label{
    color: #000;
    float: left;
    width: 75px;
    padding-right: 10px;
    text-align: right;
    margin-top: 6px;
  }
  .input-group-sm{
    position: relative;
    z-index: 0;
    padding-bottom: 10px;
    width: 80%;
    height: auto;
    margin-left: 75px;
  }
  #time{background: #fff;}
  .time{margin-bottom: 15px;}
  #accurateTime{background: #fff;}
  .accurateTime{height: 40px;}
  .search .btn{
    width: 414px;
    height: 36px;
    background-color: #769164;
    text-align: center;
    font-size: 14px;
    border-radius: 4px;
    color: #fff;
  }
  .search .btn:hover{color: #fff;}
  .input-group-addon:hover{cursor: pointer;}
  .calendar{
    position: absolute;
    z-index: 9999;
    width: 56%;
    height: 80%;
    top: 77px;
    left: 90%;
  }
  .allmap{
    width: 600px;
    height: 430px;
    overflow: hidden;
    position: absolute;
    z-index: 99;
    left: 90%;
    top:0;
    border-radius: 5px;
  }
}
/*手机端*/
@media screen and (max-width: 767px){
  #pc{
    display: none;
  }
  .head{
    width: 100%;
    text-align: center;
    background: #769164;
    color: #fff;
    font-weight: bold;
    font-size: 17px;
    line-height: 54px;
    margin-bottom: 30px;
  }
  .site,.time,.accurateTime,.search{
    margin: 0 30px;
  }
  .input-group-addon{
    width: 16%;
    border-radius: 5px;
    border: none;
    font-size: 14px;
  }
  .input-group-addon:hover{
    cursor: pointer;
  }
  .input-group{
    margin-bottom: 20px;
    border-radius: 30px;
    overflow: hidden;
    border: 1px solid #ccc;
  }
  .input-group .form-control{
    border: none;
    position: relative;
    z-index: 0;
  }
  .time{position: relative;}
  .phone_calendar{
    position: absolute;
    z-index: 999999;
    width: 80%;
    top: 32px;
    left: 10px;
  }
  .search{position: relative;}
  .search .btn{
    width: 100%;
    background-color: #769164;
    text-align: center;
    line-height: 20px;
    border-radius: 30px;
    color: #fff;
    font-size: 16px;
  }
}
</style>
