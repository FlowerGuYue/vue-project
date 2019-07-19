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
          <div class="col-lg-3 input-group"  @click="getCalendar" style="position: relative;">
            <input readonly="readonly" type="text" :value="msgDate" id="time" class="form-control" placeholder="yyyy-mm-dd">
            <span class="input-group-addon"><span class="glyphicon glyphicon-calendar" aria-hidden="true"></span></span>
            <Calendar  class="calendar" v-show="calFlag"
                v-on:choseDay="clickDay"
                :sundayStart="true"
            ></Calendar>
          </div>
          <div class="col-lg-2 buju" style="width:280px" @click="getAccurateTime">
            <TimePicker v-on:hour="hour" v-on:minute="minute" v-on:timeHour="timeHour" v-on:timeMinute="timeMinute"/>
          </div>
          <div class="col-lg-1 buju"></div>
        </div>
    	</div>
      <div class="container-fluid search_box2">
        <div id="selected">
          <select id="sel" @change="checkedParent()">
            <option v-for="opt in option" :value="opt.id" :name="opt.name">{{opt.name}}</option>
          </select>
        </div>
        <span class="check" v-for="cate in category">
          <input  @click="checkedSonItem(cate)" type="checkbox" :name="cate.name" :value="cate.id" v-model="cate.sta"/>{{cate.name}}
        </span>
        <div style="position: relative;width:250px;height:40px;float: right;">
          <img id="loading" style="left:55px;bottom:4px" class="loading" src="../assets/img/icon/loading (2).gif" alt="加载中……">
          <div @click="search" class="search"><a class="btn">查询</a></div>
        </div>
      </div>
      <!-- 方案 -->
      <div class="routes">
    		<p>方案推荐</p>
    		<div class="tips" v-for="mMsg,index in msg">
          <!-- 飞机 -->
          <div v-if="mMsg.lineInfoFlag==1||mMsg.lineInfoFlag==2" class="detail_info">
            <blockquote>
              起点：{{mMsg.startLineInfoBean.lineInfoStart}}<br/>
              终点：{{mMsg.endLineInfoBean.lineInfoEnd}}<br/>
              {{formatSeconds(mMsg.lineInfoTimes)}} ￥{{mMsg.lineInfoPrice}}
            </blockquote>
            <!-- 从起点到A地车站 -->
            <ul v-for="mDetail in mMsg.startLineInfoBean.shortLines">
              <li v-if="mDetail.shortLineType==3"><!--公交-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/公交.svg" alt="">
                  <p style="margin:0;width:306px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}——大约{{formatSeconds(mDetail.shortLineTimes)}}</p>
                  <p>{{mDetail.shortLineVehicleNum}}【{{mDetail.shortLineVehicleTimeTable}}】</p>
                </div>
              </li>
              <li v-if="mDetail.shortLineType==4"><!--驾车-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/大巴.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                  <p>{{mDetail.shortLineVehicleNum}}</p>
                </div>
              </li>
              <li v-if="mDetail.shortLineType==5"><!--步行-->
                <div class="box">
                  <p>步行的起点{{mMsg.startLineInfoBean.shortLineStart}}</p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/步行.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#416367;font-weight:bold;margin:0">{{mDetail.shortLineVehicleInfo}}</p>
                  <p>大约{{formatSeconds(mDetail.shortLineTimes)}}</p>
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
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>{{mDetail.shortLineVehicleNum}}</p>
                  </div>
                </li>
            </ul>
            <ul v-for="mDetail in mMsg.shortLines">
                <li v-if="mDetail.shortLineType==1"><!--火车-->
                  <div class="box">
                    <p>{{mDetail.shortLineStart}}</p>
                    <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                  </div>
                  <div class="box">
                    <img src="../assets/img/icon/plan/火车.svg" alt="">
                    <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>{{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}-{{mDetail.shortLineVehicleNum}}</p>
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
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>{{mDetail.shortLineStartTime}}-{{mDetail.shortLineStartTime}}-{{mDetail.shortLineVehicleNum}}</p>
                  </div>
                </li>
                <li v-if="mDetail.shortLineType==3"><!--公交-->
                  <div class="box">
                    <p>{{mDetail.shortLineStart}}</p>
                    <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                  </div>
                  <div class="box">
                    <img src="../assets/img/icon/plan/公交.svg" alt="">
                    <p style="margin:0;width:306px;height:1px;;border:1px solid #000;"></p>
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>({{mDetail.shortLineVehicleTimeTable}}){{mDetail.shortLineVehicleNum}}</p>
                  </div>
                </li>
                <li v-if="mDetail.shortLineType==4"><!--驾车-->
                  <div class="box">
                    <p>{{mDetail.shortLineStart}}</p>
                    <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                  </div>
                  <div class="box">
                    <img src="../assets/img/icon/plan/大巴.svg" alt="">
                    <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>{{mDetail.shortLineVehicleNum}}</p>
                  </div>
                </li>
                <li v-if="mDetail.shortLineType==5"><!--步行-->
                  <div class="box">
                    <p>{{mDetail.shortLineStart}}</p>
                    <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                  </div>
                  <div class="box">
                    <img src="../assets/img/icon/plan/步行.svg" alt="">
                    <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                    <p style="color:#416367;font-weight:bold;margin:0">步行-用时{{mDetail.shortLineTimes}}分</p>
                    <p>{{mDetail.shortLineLength}}米</p>
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
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>{{mDetail.shortLineVehicleNum}}</p>
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
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>({{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}){{mDetail.shortLineVehicleNum}}</p>
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
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>{{mDetail.shortLineVehicleNum}}</p>
                  </div>
                </li>
            </ul>
            <ul v-for="mDetail in mMsg.endLineInfoBean.shortLines">
                <li v-if="mDetail.shortLineType==1"><!--火车-->
                  <div class="box">
                    <p>{{mDetail.shortLineStart}}</p>
                    <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                  </div>
                  <div class="box">
                    <img src="../assets/img/icon/plan/火车.svg" alt="">
                    <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>{{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}-{{mDetail.shortLineVehicleNum}}</p>
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
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>{{mDetail.shortLineStartTime}}-{{mDetail.shortLineStartTime}}-{{mDetail.shortLineVehicleNum}}</p>
                  </div>
                </li>
                <li v-if="mDetail.shortLineType==3"><!--公交-->
                  <div class="box">
                    <p>{{mDetail.shortLineStart}}</p>
                    <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                  </div>
                  <div class="box">
                    <img src="../assets/img/icon/plan/公交.svg" alt="">
                    <p style="margin:0;width:306px;height:1px;;border:1px solid #000;"></p>
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>({{mDetail.shortLineVehicleTimeTable}}){{mDetail.shortLineVehicleNum}}</p>
                  </div>
                </li>
                <li v-if="mDetail.shortLineType==4"><!--驾车-->
                  <div class="box">
                    <p>{{mDetail.shortLineStart}}</p>
                    <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                  </div>
                  <div class="box">
                    <img src="../assets/img/icon/plan/大巴.svg" alt="">
                    <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>{{mDetail.shortLineVehicleNum}}</p>
                  </div>
                </li>
                <li v-if="mDetail.shortLineType==5"><!--步行-->
                  <div class="box">
                    <p>{{mDetail.shortLineStart}}</p>
                    <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                  </div>
                  <div class="box">
                    <img src="../assets/img/icon/plan/步行.svg" alt="">
                    <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                    <p style="color:#416367;font-weight:bold;margin:0">步行-用时{{mDetail.shortLineTimes}}分</p>
                    <p>{{mDetail.shortLineLength}}米</p>
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
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>{{mDetail.shortLineVehicleNum}}</p>
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
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>({{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}){{mDetail.shortLineVehicleNum}}</p>
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
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>{{mDetail.shortLineVehicleNum}}</p>
                  </div>
                </li>
            </ul>
            <ul v-for="mDetail in mMsg.endLineInfoBean.endLineInfoBean.shortLines">
                <li v-if="mDetail.shortLineType==1"><!--火车-->
                  <div class="box">
                    <p>{{mDetail.shortLineStart}}</p>
                    <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                  </div>
                  <div class="box">
                    <img src="../assets/img/icon/plan/火车.svg" alt="">
                    <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>{{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}-{{mDetail.shortLineVehicleNum}}</p>
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
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>{{mDetail.shortLineStartTime}}-{{mDetail.shortLineStartTime}}-{{mDetail.shortLineVehicleNum}}</p>
                  </div>
                </li>
                <li v-if="mDetail.shortLineType==3"><!--公交-->
                  <div class="box">
                    <p>{{mDetail.shortLineStart}}</p>
                    <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                  </div>
                  <div class="box">
                    <img src="../assets/img/icon/plan/公交.svg" alt="">
                    <p style="margin:0;width:306px;height:1px;;border:1px solid #000;"></p>
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>({{mDetail.shortLineVehicleTimeTable}}){{mDetail.shortLineVehicleNum}}</p>
                  </div>
                </li>
                <li v-if="mDetail.shortLineType==4"><!--驾车-->
                  <div class="box">
                    <p>{{mDetail.shortLineStart}}</p>
                    <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                  </div>
                  <div class="box">
                    <img src="../assets/img/icon/plan/大巴.svg" alt="">
                    <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>{{mDetail.shortLineVehicleNum}}</p>
                  </div>
                </li>
                <li v-if="mDetail.shortLineType==5"><!--步行-->
                  <div class="box">
                    <p>{{mDetail.shortLineStart}}</p>
                    <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                  </div>
                  <div class="box">
                    <img src="../assets/img/icon/plan/步行.svg" alt="">
                    <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                    <p style="color:#416367;font-weight:bold;margin:0">步行-用时{{mDetail.shortLineTimes}}分</p>
                    <p>{{mDetail.shortLineLength}}米</p>
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
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>{{mDetail.shortLineVehicleNum}}</p>
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
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>({{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}){{mDetail.shortLineVehicleNum}}</p>
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
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>{{mDetail.shortLineVehicleNum}}</p>
                  </div>
                </li>
            </ul>
            <!-- 终点 -->
            <div class="last">
              <img src="../assets/img/icon/9终点.svg" alt="">
              <p>{{mMsg.endLineInfoBean.lineInfoEnd}}</p>
            </div>
          </div>
          <!-- 火车/高铁 -->
          <div v-if="mMsg.lineInfoFlag==0" class="detail_info">
            <blockquote>
              起点：{{mMsg.startLineInfoBean.lineInfoStart}}<br/>
              终点：{{mMsg.endLineInfoBean.lineInfoEnd}}<br/>
              {{formatSeconds(mMsg.lineInfoTimes)}} ￥{{mMsg.lineInfoPrice}}
            </blockquote>
            <!-- 从起点到A地车站 -->
            <ul v-for="mDetail,index in mMsg.startLineInfoBean.shortLines">
              <li v-if="mDetail.shortLineType==3"><!--公交-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/公交.svg" alt="">
                  <p style="margin:0;width:306px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}——大约{{formatSeconds(mDetail.shortLineTimes)}}</p>
                  <p>{{mDetail.shortLineVehicleNum}}【{{mDetail.shortLineVehicleTimeTable}}】</p>
                </div>
              </li>
              <li v-if="mDetail.shortLineType==4"><!--驾车-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/大巴.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                  <p>{{mDetail.shortLineVehicleNum}}</p>
                </div>
              </li>
              <li v-if="mDetail.shortLineType==5"><!--步行-->
                <div class="box">
                  <p v-if="index==0">{{mMsg.startLineInfoBean.lineInfoStart}}</p>
                  <p v-if="index!=0">{{mDetail.shortLineStart}}</p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/步行.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#416367;font-weight:bold;margin:0">{{mDetail.shortLineVehicleInfo}}</p>
                  <p>大约{{formatSeconds(mDetail.shortLineTimes)}}</p>
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
                    <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                    <p>{{mDetail.shortLineVehicleNum}}</p>
                  </div>
                </li>
            </ul>
            <!-- 从A地车站到B地车站 -->
            <ul v-for="mDetail in mMsg.shortLines">
              <li v-if="mDetail.shortLineType==1"><!--火车-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/火车.svg" alt="">
                  <p style="margin:0;width:190px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}——{{formatSeconds(mDetail.shortLineTimes)}}</p>
                  <p>【{{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}】{{mDetail.shortLineVehicleNum}}</p>
                </div>
              </li>
              <li v-if="mDetail.shortLineType==4"><!--驾车-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/大巴.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                  <p>{{mDetail.shortLineVehicleNum}}</p>
                </div>
              </li>
              <li v-if="mDetail.shortLineType==5"><!--步行-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/步行.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#416367;font-weight:bold;margin:0">{{mDetail.shortLineVehicleInfo}}</p>
                  <p>大约{{formatSeconds(mDetail.shortLineTimes)}}</p>
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
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                  <p>{{mDetail.shortLineVehicleNum}}</p>
                </div>
              </li>
            </ul>
            <!-- 从B地到终点 -->
            <ul v-for="mDetail,index in mMsg.endLineInfoBean.shortLines">
              <li v-if="mDetail.shortLineType==1"><!--火车-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/火车.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                  <p>{{mDetail.shortLineStartTime}}-{{mDetail.shortLineEndTime}}-{{mDetail.shortLineVehicleNum}}</p>
                </div>
              </li>
              <li v-if="mDetail.shortLineType==3"><!--公交-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/公交.svg" alt="">
                  <p style="margin:0;width:306px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}——大约{{formatSeconds(mDetail.shortLineTimes)}}</p>
                  <p>{{mDetail.shortLineVehicleNum}}【{{mDetail.shortLineVehicleTimeTable}}】</p>
                </div>
              </li>
              <li v-if="mDetail.shortLineType==4"><!--驾车-->
                <div class="box">
                  <p>{{mDetail.shortLineStart}}</p>
                  <p style="width:8px;height:8px;background:#555;margin:auto;border-radius:50%"></p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/大巴.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                  <p>{{mDetail.shortLineVehicleNum}}</p>
                </div>
              </li>
              <li v-if="mDetail.shortLineType==5"><!--步行-->
                <div class="box">
                  <p v-if="index==0">{{mMsg.endLineInfoBean.lineInfoStart}}</p>
                  <p>{{mDetail.shortLineStart}}</p>
                </div>
                <div class="box">
                  <img src="../assets/img/icon/plan/步行.svg" alt="">
                  <p style="margin:0;width:150px;height:1px;;border:1px solid #000;"></p>
                  <p style="color:#416367;font-weight:bold;margin:0">{{mDetail.shortLineVehicleInfo}}</p>
                  <p>大约{{formatSeconds(mDetail.shortLineTimes)}}</p>
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
                  <p style="color:#862537;font-weight:bold;margin:0">￥{{mDetail.shortLinePrice}}-用时{{mDetail.shortLineTimes}}</p>
                  <p>{{mDetail.shortLineVehicleNum}}</p>
                </div>
              </li>
            </ul>
            <!-- 终点 -->
            <div class="last">
              <img src="../assets/img/icon/9终点.svg" alt="">
              <p>{{mMsg.endLineInfoBean.lineInfoEnd}}</p>
            </div>
            <button id="detailIndex" @click="feedback(index)">查看详细路径</button>
          </div>
    		</div>
    	</div>
    </div>
    <div v-else class="noData">
      <img src="../assets/img/没有路线.png" alt="">
      <h1>当前查询路线为空</h1>
    </div>
	  <div class="mobile"></div>
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
      msg: [],//路线信息

      flag: true,
      calFlag: false,
      msgDate: '',
      indexFlag: true,

      changeHour:'',// 具体时间
      changeMinute:'',
      curHour:'',
      curMinute:'',

      startPoint: '',// 起始坐标
      endPoint: '',// 终点坐标
      city_code: '',//城市id
      city_code2: '',
      option: [
        {id: 0, name: '其他',selected:true},
        {id: 1, name: '商务旅行'},
        {id: 2, name: '单人旅行'},
        {id: 3, name: '家庭出游'}
      ],
      category: [
        {id: 0, name: '时间短', sta: false},
        {id: 1, name: '价格低', sta: false},
        {id: 2, name: '路程短', sta: false},
        {id: 3, name: '较舒适', sta: false}
      ],
      arr2: [
        [
          //其他
        ],
        [
          //商务旅行
          0,1
        ],
        [
          //单人旅行
          1
        ],
        [
          //家庭出游
          2,3
        ]
      ]
    }
  },
  created(){
    this.start();
    this.end();
  },
  mounted(){
    let that=this;
    let planStr = sessionStorage.getItem('plan');
    let planObj = JSON.parse(planStr);
    // 路线信息
    that.msg = planObj.lineInfoList;
    if (that.msg==''|| that.msg==null) {that.flag = false;}
  },
  methods:{
    // 选框
    checkedParent: function() {
      let that=this;
      //选择的出行场景id
      let num=Number(sel.options[sel.selectedIndex].value);
      //arr就是 当前出行场景 对应的 条件id数组
      let arr =  that.arr2[num];
      //将所有条件选择框重置为false
      that.category.forEach(function(info) {info.sta = false});

      for( var i=0;i<arr.length;i++){
        that.category.forEach(function(info) {
          if(info.id == arr[i]){
            info.sta = true;
          }
        });
      }
    },
    checkedSonItem: function(info) {
      if(info.sta){
        info.sta = false;
      }else{
        info.sta = true;
      }

      let len = 0;
      this.category.forEach(function(item) {
        if(item.sta==true){
          len++;
        }
      });
      let arr = new Array(len);
      let n = 0;
      this.category.forEach(function(item) {
        if (item.sta==true) {
          arr[n] = item.id;
          n++;
        }
      });

      //arr 就是所有的选中的出行条件的id数组
      //遍历arr2
      for(let i=0;i<this.arr2.length;i++){
        //bean是一个出行场景
        let bean = this.arr2[i];
        //判断当前出行场景id数组arr  是否与  选中的出行条件的id数组bean 完全相同（顺序可以不同）
        if( this.isContained(arr,bean) ){
          for(let f=0;f<sel.length;f++){
            sel[f].selected = false;
          }
          sel[i].selected = true;
          return;
        }
      }
      // 遍历option,让所有选项都隐藏
      for(let f=0;f<sel.length;f++){
        sel[f].selected = false;
      }
      //将“其他”选项显示
      sel[0].selected = true;
    },
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
    // 比较两个数组
    isContained(aa, bb) {
      for(var i = 0;i<bb.length;i++){
        var num = 0;
        for(var j=0;j<aa.length;j++){
          if(bb[i] == aa[j]){
            num++;
          }
        }
        if(num < 1){
          return false;
        }
      }
      for(var i = 0;i<aa.length;i++){
        var num = 0;
        for(var j=0;j<bb.length;j++){
          if(bb[j] == aa[i]){
            num++;
          }
        }
        if(num < 1){
          return false;
        }
      }
      return true;
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
    getCalendar:function(){//获取日历
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

      let typeList = '';
      that.category.forEach(function(info) {
        if (info.sta) {
          typeList += info.id+',';
        }
      });

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
          url: 'http://192.168.1.101:65525/otherCity.line',
          headers: {'Content-Type': 'application/x-www-form-urlencoded'},
          data: {
            endCid: code2,
            endPoint: bb,
            startCid: code,
            startPoint: aa,
            startTime: c+""+q,
            tripTypeList: typeList
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
    // 发表评论
    feedback:function(index){
      let that=this;
      sessionStorage.setItem("feedback",JSON.stringify(that.msg[index]));
      that.$router.push({path:'/feedback'});
    }
  }
}
</script>

<style lang="css" scoped>
.bestx{
  position: absolute;
  top: 0;
  left: 0;
  width: 110px;
  height: 110px;
  position: relative;
  transform:rotate(-41deg)translate(0,-106px);
  background: red;
  color: #fff;
  font-weight: bold;
}
.bestx>p{
  width: 100%;
  text-align: center;
  margin: 5px 0;
  position: absolute;
  bottom: 0;
}
/*pc端*/
@media screen and (min-width: 768px){
  #detailIndex{
    margin: 20px 40px;
    width: 150px;
    height: 40px;
    border-radius: 4px;
    background: #769164;
    color: #fff;
    border: none;
  }
  #selected{
    width: 150px;
    height: 30px;
    /* box-shadow: 0 0 5px #ccc; */
    position: relative;
    color: #393e46;
    display: inline-block;
  }
  #selected>select{
    border: none;
    /* 清除select聚焦时候的边框颜色 */
    outline: none;
    width: 100%;
    height: 30px;
    border-radius: 4px;
    line-height: 30px;
    /* 隐藏select的下拉图标 */
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    text-align: center;
  }
  .check{margin-left: 17px;}
  .box{float: left;}
  .mobile{display: none;}
  .pc{
    padding-top: 100px;
    padding-bottom: 85px;
    background: url('../assets/img/bg-pc.jpg');
    background-repeat: no-repeat;
    background-size: cover;
    background-attachment: fixed;
  }
	a:hover,a:focus{text-decoration: none;}
  li{float: left;list-style: none;}
  .search_box{
    width: 80%;
    padding: 20px;
		background: #eef1f8;
		border: 1px solid #769164;
		border-radius: 4px;
    margin: 0 auto 20px;
	}
  .search_box2{
    width: 80%;
    padding: 20px;
    margin: 0 auto 20px;
    color: #fff;
    font-size: 16px;
    position: relative;
  }
  .search{
    width: 250px;
    margin-right: 77px;
  }
  .input-group{
    padding:0 20px;
    margin: auto;
  }
  .form-control{
    background: #fff;
  }
  .calendar{
    position: absolute;
    z-index: 9999;
    top: 40px;
    left: 0;
  }
  .buju{height: 35px;}
  .btn{
    width: 100%;
    background-color: #769164;
    text-align: center;
    font-size: 14px;
    border-radius: 4px;
    color: #fff;
    font-weight: bold;
  }
	/* 路线方案 */
	.routes{
    width: 80%;
    margin: 0 auto;
	}
	.routes>p{
    margin: 10px 0px 0px;
    color: #eee;
    font-size: 16px;
	}
  .routes:nth-child(1)>.tips{
    background: #769164;
  }
	.tips{
    position: relative;
		padding:20px;
		background: #eef1f8;
		margin-top: 10px;
		border: 1px solid #769164;
		border-radius: 10px;
		display: flex;
		flex-wrap: wrap;
    overflow: hidden;
	}
  .tips:hover .detail_info{
    /* box-shadow: 10px 10px 5px #888888; */
    box-shadow: darkgrey 10px 10px 30px 5px;
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
  .noData{
    margin: auto;
    width: 35%;
    color: #fff;
  }
  .noData>img{
    width: 500px;
    height: 500px;
  }
  .noData>h1{
    margin: 0;
    text-align: center;
  }
}
/*手机端*/
@media screen and (max-width: 767px){
 .pc{display: none;}
 .mobile{padding-top: 58px;}
 /* 路线方案 */
 .routes{
   width: 90%;
   margin: 0 auto;
 }
 .routes p{
   margin: 20px 0px 0px;
 }
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
 .current{text-align: center;}
 .current img{
   width: 20px;
   height: 20px;
   margin-top: 10px;
 }
 .current>span{
   display: block;
   line-height: 22px;
 }
 .routes_line{
   position: relative;
   z-index: 1;
 }
 .routes_line .dot-route{
   width: 120px;
   height: 50px;
   opacity: 0.7;
 }
 .foot_info,.foot_time{
   text-align: center;
   width: 88%;
   position: absolute;
   left:0;
 }
 .foot_info{top:-12px;}
 .foot_time{top:12px;}
}
</style>
