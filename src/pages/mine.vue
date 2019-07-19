<template lang="html">
<div>
  <div v-if="this.isLogin!=1">
    <LoginNo/>
  </div>
  <div v-if="this.isLogin==1">
    <Menux :tabs="tabs">
      <template slot="tab1">
        <table>
          <thead>
            <tr>
              <!-- 男的 -->
              <td class="avatar" v-if="msg.userImgpath==''&&msg.userSex==0">
                <img src="http://47.110.225.74/userImg/boy.svg" alt="">
              </td>
              <!-- 女的 -->
              <td class="avatar" v-else-if="msg.userImgpath==''&&msg.userSex==1">
                <img src="http://47.110.225.74/userImg/girl.svg" alt="">
              </td>
              <td class="avatar" v-else="msg.userImgpath!=''">
                <img :src="msg.userImgpath" alt="">
              </td>
              <td><a href="#" class="btn" @click="showIconBox">更改头像</a></td>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="set_title">昵称</td>
              <td id="mUsername">{{msg.userUsername}}</td>
              <td><a href="#" class="btn" @click="showUsernameBox">修改昵称</a></td>
            </tr>
            <tr>
              <td class="set_title">手机号</td>
              <td class="num">
                <div class="phoneNum">{{msg.userTel}}</div>
                <i></i>
                <span style="color:#eee">已验证</span>
              </td>
              <td><a href="#" @click="showTalBox">更换绑定的手机号</a></td>
            </tr>
            <tr>
              <td class="set_title">密码</td>
              <td id="mPassword">*********</td><!-- {{msg.userPassword}} -->
              <td><a href="#" class="btn" @click="showPasswordBox">修改密码</a></td>
            </tr>
            <tr>
              <td class="set_title">邮箱</td>
              <td id="mEmail">{{msg.userEmail}}</td>
              <td><a href="#" class="btn" @click="showEmailBox">点击绑定</a></td>
            </tr>
            <tr v-show="this.flag">
              <td class="set_title">姓名</td>
              <td id="">xxxx</td>
            </tr>
            <tr v-show="this.flag">
              <td class="set_title">性别</td>
              <td id="">xxxx</td>
            </tr>
            <tr v-show="this.flag">
              <td class="set_title">身份证号</td>
              <td id="">xxxx</td>
            </tr>
          </tbody>
          <!-- 完善个人信息按钮 -->
          <!-- <input v-show="this.flagbtn" class="addInfo" type="submit" @click="showAddInfoBox" value="完善信息"> -->
          <!-- 弹框 -->
          <article class="iframe">
            <img id="loading" class="loading1" src="../assets/img/icon/loading.gif" alt="加载中……">
            <img class="closeImg" src="../assets/img/icon/叉叉.png" @click="close" alt="关闭">
            <section id="iconBox">
              <div class="box"><img id="imgshow" src="" alt="头像"/></div>
              <div class="pox">
                <input type="file" @change="myIcon" id="filed" value="选择图片" accept="image/*"/>
              </div>
              <button class="mbtn" @click="complete_myIcon">上传</button>
            </section>
            <section id="usernameBox">
              <div class="form-group">
                <input type="text" id="username" class="form-control" placeholder="昵称">
              </div>
              <div class="form-group">
                <button class="mbtn" @click="complete_username">完成</button>
              </div>
            </section>
            <section id="telBox">
              <div class="form-group">
                <input type="tel" id="oldTel" style="background:transparent;" :value="msg.userTel" disabled class="form-control buju" placeholder="手机号">
              </div>
              <div class="form-group">
                <input type="text" id="tel_code" class="form-control code" placeholder="验证码">
                <button class="getCode" v-bind:class="{gray:wait_timer>0}" @click="get_telCode">{{text()}}</button>
              </div>
              <div class="form-group">
                <input type="tel" id="newTel" @blur="phoneNumber2" class="form-control buju" placeholder="新手机号">
                <span id="numTishi2"></span>
              </div>
              <div class="form-group">
                <button class="mbtn" @click="complete_tel">完成</button>
              </div>
            </section>
            <section id="passwordBox">
              <div class="form-group">
                <input type="tel" id="myNum" style="background:transparent;" :value="msg.userTel" disabled class="form-control buju" placeholder="手机号">
              </div>
              <div class="form-group">
                <input type="password" id="newPassword" @blur="pwd" class="form-control buju" placeholder="新密码">
                <span  id="pwdTishi">8-16位数字或字母</span>
              </div>
              <div class="form-group">
                <input type="password" id="reNewPassword" @blur="repwd" class="form-control buju" placeholder="确认密码">
                <span id="repwdTishi">再次输入密码</span>
              </div>
              <div class="form-group">
                <input type="text" id="password_code" class="form-control code" placeholder="验证码">
                <button class="getCode" v-bind:class="{gray:wait_timer>0}" @click="get_passwordCode">{{text()}}</button>
              </div>
              <div class="form-group">
                <button class="mbtn" @click="complete_password">完成</button>
              </div>
            </section>
            <section id="emailBox">
              <div class="form-group">
                <input type="text" id="bindEmail" class="form-control" placeholder="邮箱">
              </div>
              <div class="form-group">
                <input type="text" class="form-control code" id="email_code" placeholder="验证码">
                <button class="getCode" v-bind:class="{gray:wait_timer>0}" @click="get_emailCode">{{text()}}</button>
              </div>
              <div class="form-group">
                <button class="mbtn" @click="complete_bindEmail">完成</button>
              </div>
            </section>
            <!-- 完善个人信息弹框 -->
            <!-- <section id="addInfoBox">
              <div class="form-group">
                <input style="width: 20%" id="male" type="radio" name="sex" value="男" checked>男
                <input style="width: 20%" id="female" type="radio" name="sex" value="女">女
              </div>
              <div class="form-group">
                <button class="mbtn" @click="complete_addInfo">完成</button>
              </div>
            </section> -->
          </article>
        </table>
      </template>
      <template slot="tab2">
        <figure>
          <img class="noDataImg" src="../assets/img/无数据.png" alt="">
          <span class="noDataTxt">还没有订单哦~</span>
        </figure>
        <!-- 订单列表 -->
        <table style="display:none;">
          <thead></thead>
          <tbody>
            <tr>
              <td></td>
            </tr>
          </tbody>
        </table>
        <ol>
          <li></li>
        </ol>
      </template>
      <template slot="tab3">
        <div class="figure" @click="addMan">
          <img class="addImg" src="../assets/img/icon/add.png" alt="添加抢票">
          <span class="addTxt">添加乘客</span>
        </div>
        <table style="width: 80%;margin: 50px 20px;position: relative;">
          <thead>
            <button id="freshMan" class="btn" @click="searchMan">刷新乘客信息</button>
          </thead>
          <tbody>
            <!-- 购票人列表 -->
            <tr v-for="man,index in mans">
              <td class="set_title">{{man.buyerName}}</td>
              <td>身份证号：{{man.idCard}}</td>
              <td class="set_title">
                <span v-if="man.buyerSex==0">男</span>
                <span v-if="man.buyerSex==1">女</span>
              </td>
              <td class="set_title">
                <a href="#" class="btn" @click="deletMan(man.idCard,index)">删除</a>
              </td>
            </tr>
            <!-- 弹框 -->
            <article class="iframe">
              <img id="loading" class="loading2" src="../assets/img/icon/loading.gif" alt="加载中……">
              <img class="closeImg" src="../assets/img/icon/叉叉.png" @click="close" alt="关闭">
              <section id="addManBox">
                <div class="form-group">
                  <input type="text" id="myName" class="form-control buju" placeholder="姓名">
                  <span>请填写身份证上的姓名</span>
                </div>
                <div class="form-group">
                  <input type="text" id="myId" class="form-control" placeholder="身份证号">
                </div>
                <div class="form-group">
                  <input style="width: 20%" id="male" type="radio" name="sex" value="0" checked>男
                  <input style="width: 20%" id="female" type="radio" name="sex" value="1">女
                </div>
                <div class="form-group">
                  <button class="mbtn" @click="complete_addMan">完成</button>
                </div>
              </section>
            </article>
          </tbody>
        </table>
      </template>
      <template slot="tab4">
        联系客服
        <img style="width: 300px;height: 300px;display: block;margin: auto;" src="../assets/img/idea.png" alt="未登录">
        <p style="width: 180px;height: 20px;font-size: 16px;margin: auto;color: #eee;">
          正在开发中，敬请期待！
        </p>
      </template>
    </Menux>
  </div>
</div>
</template>

<script>
import {SERVER} from '@/config';
import LoginNo from '@/components/loginNo';
import Menux from '@/components/menux';

export default {
  name: 'mine',
  components: { LoginNo, Menux },
  data(){
    return {
      tabs: [
        {title: '个人信息', slotname: 'tab1'},
        {title: '我的订单', slotname: 'tab2'},
        {title: '常用购票人', slotname: 'tab3'},
        {title: '联系客服', slotname: 'tab4'}
      ],
      isLogin: '',
      msg: [], // 登陆后信息
      wait_timer: false, //发送验证码倒计时
      flag: false,  // 完善的信息内容隐藏
      flagbtn: true,  // 完善信息按钮显示
      mans: []  //添加乘客的信息
    }
  },
  created(){
    this.isLogin = sessionStorage.getItem('log');
  },
  mounted(){
    let userStr = sessionStorage.getItem('user');
    this.msg = JSON.parse (userStr);
  },
  methods: {
    // 验证码
    sendCode:function(){
      if (this.wait_timer > 0) {
        return false;
      }
      this.wait_timer = 59;
      var that = this;
      var timer_interval = setInterval(function(){
        if(that.wait_timer > 0){
          that.wait_timer -- ;
        }else{
          clearInterval(timer_interval);
        }
      },1000);
    },
    text(){
      if(this.wait_timer > 0){
        return this.wait_timer+'s后获取';
      }
      if(this.wait_timer === 0){
        return '重新获取';
      }
      if(this.wait_timer === false){
        return '获取验证码';
      }
    },
    // 点击显示弹框
    showIconBox(){
      $(".iframe").css("display","block");
      $("#iconBox").css("display","block");

      $("#usernameBox").css("display","none");
      $("#telBox").css("display","none");
      $("#passwordBox").css("display","none");
      $("#emailBox").css("display","none");
      $("#addInfoBox").css("display","none");
      $("#addManBox").css("display","none");
    },
    showUsernameBox(){
      $(".iframe").css("display","block");
      $("#usernameBox").css("display","block");

      $("#iconBox").css("display","none");
      $("#telBox").css("display","none");
      $("#passwordBox").css("display","none");
      $("#emailBox").css("display","none");
      $("#addInfoBox").css("display","none");
      $("#addManBox").css("display","none");

      $("#username").val("");
    },
    showTalBox(){
      $(".iframe").css("display","block");
      $("#telBox").css("display","block");

      $("#usernameBox").css("display","none");
      $("#iconBox").css("display","none");
      $("#passwordBox").css("display","none");
      $("#emailBox").css("display","none");
      $("#addInfoBox").css("display","none");
      $("#addManBox").css("display","none");

      $('#newTel').val("");
      $('#tel_code').val("");
    },
    showPasswordBox(){
      $(".iframe").css("display","block");
      $("#passwordBox").css("display","block");

      $("#iconBox").css("display","none");
      $("#usernameBox").css("display","none");
      $("#telBox").css("display","none");
      $("#emailBox").css("display","none");
      $("#addInfoBox").css("display","none");
      $("#addManBox").css("display","none");

      $('#newPassword').val("");
      $('#reNewPassword').val("");
      $('#password_code').val("");
    },
    showEmailBox(){
      $(".iframe").css("display","block");
      $("#emailBox").css("display","block");

      $("#iconBox").css("display","none");
      $("#usernameBox").css("display","none");
      $("#telBox").css("display","none");
      $("#passwordBox").css("display","none");
      $("#addInfoBox").css("display","none");
      $("#addManBox").css("display","none");

      $("#bindEmail").val("");
      $("#email_code").val("");
    },
    // showAddInfoBox(){
    //   $(".iframe").css("display","block");
    //   $("#addInfoBox").css("display","block");
    //
    //   $("#iconBox").css("display","none");
    //   $("#usernameBox").css("display","none");
    //   $("#telBox").css("display","none");
    //   $("#passwordBox").css("display","none");
    //   $("#emailBox").css("display","none");
    // },

    // 关闭
    close(){$(".iframe").css("display","none");},

    // 上传头像
    myIcon(){
      //获取input file的files文件数组;
      //$('#filed')获取的是jQuery对象，.get(0)转为原生对象;
      //这边默认只能选一个，但是存放形式仍然是数组，所以取第一个元素使用[0];
      var file = $('#filed').get(0).files[0];
      //创建用来读取此文件的对象
      var reader = new FileReader();
      //使用该对象读取file文件
      reader.readAsDataURL(file);
      //读取文件成功后执行的方法函数
      reader.onload=function(e){
        //读取成功后返回的一个参数e，整个的一个进度事件
        // console.log(e);
        //选择所要显示图片的img，要赋值给img的src就是e中target下result里面
        //的base64编码格式的地址
        $('#imgshow').get(0).src = e.target.result;
      }
    },
    complete_myIcon(){
      let that=this;
      var formData = new FormData();
      formData.append('userId',JSON.parse(sessionStorage.getItem('user')).userId);
			formData.append('headPic',$("#filed")[0].files[0]);
      $(".loading1").css("display","block");
      $(".mbtn").css("background","#fff");
			$.ajax({
	        url: SERVER+'traveler/alterUserHeadImgAction',
	        type: 'POST',
	        cache: false,
	        data: formData,
	        processData: false,
	        contentType: false,
	        success : function(data){
            sessionStorage.setItem('user',JSON.stringify(data.loginedUser));
            alert("上传成功");
            that.msg.userImgpath=data.loginedUser.userImgpath;
            $(".iframe").css("display","none");
            $(".loading1").css("display","none");
            $(".mbtn").css("background","#769164");
	        },
	        error : function(){
	        	alert("上传失败，请检查网络");
            $(".iframe").css("display","none");
            $(".loading1").css("display","none");
            $(".mbtn").css("background","#769164");
	        }
			});

      // let that=this;
      // this.axios({
      //   method: 'post',
      //   url: SERVER+'traveler/alterUserHeadImgAction',
      //   data:formData,
      //   headers: {'Content-Type': 'multipart/form-data;boundary=2'},
      // }).then(function (res) {
      //   if(res.data.code == 0){
      //     alert(res.data.errorMsg);
      //   }else if (res.data.code == -1) {
      //     alert("系统异常，请稍后再试");
      //   }else if(res.data.code == 1){
      //     alert("修改成功");
      //     $(".iframe").css("display","none");
      //   }
      // }).catch(function (err) {
      //   alert("服务器出错了，请稍后再试");
      // });
    },

    // 修改昵称
    complete_username(){
      if ( $("#username").val()=="" ){$("#username").focus();}
      else {
        $(".loading1").css("display","block");
        $(".mbtn").css("display","none");
        let that=this;
        this.axios({
          method: 'post',
          url: SERVER+'traveler/alterUserInfoAction',
          headers: {'Content-Type': 'application/x-www-form-urlencoded'},
          data: {
            userUsername: $("#username").val()
          }
        }).then(function (res) {
          if(res.data.code == 0){
            alert(res.data.errorMsg);
            $(".iframe").css("display","none");
            $(".loading1").css("display","none");
            $(".mbtn").css("background","#769164");
          }else if (res.data.code == -1) {
            alert("系统异常，请稍后再试");
            $(".iframe").css("display","none");
            $(".loading1").css("display","none");
            $(".mbtn").css("background","#769164");
          }else if(res.data.code == 1){
            alert("修改成功");
            sessionStorage.setItem('user',JSON.stringify(res.data.loginedUser));
            that.msg.userUsername=res.data.loginedUser.userUsername;
            $(".iframe").css("display","none");
            $(".loading1").css("display","none");
            $(".mbtn").css("background","#769164");
          }
        }).catch(function (err) {
          alert("服务器出错了，请稍后再试");
          $(".iframe").css("display","none");
          $(".loading1").css("display","none");
          $(".mbtn").css("background","#769164");
        });
      }
    },

    // 修改手机号
    phoneNumber2:function(){
      let re=/^1[34578]\d{9}$/;
      let re2=/^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
      let phoneNumber=$('#newTel').val();
      if ( re.test(phoneNumber) || re2.test(phoneNumber) ) {
        $('#numTishi2').text("验证成功").css("color","#eee");
      }else{
        $('#numTishi2').text("请输入正确的账号").css("color","#c97586");
      }
    },
    get_telCode(){
      let that=this;
      this.axios({
        method: 'post',
        url: SERVER+'traveler/sendVerifyCodeAction',
        data: {
          account: $("#oldTel").val(),
          type: 5
        },
        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
      })
      .then(function (res) {
        if(res.data.code == 0){
          alert(data.msg);
        }else if (res.data.code == -1) {
          alert("系统繁忙，请稍后再试");
        }else if(res.data.code == 1){
          that.sendCode();
        }
      }).catch(function (error) {
        alert("服务器出错了，请稍后再试");
      });
    },
    complete_tel(){
      let that=this;
      if ($("#newTel").val()=='') {
        $("#newTel").focus();
      }else if ($("#tel_code").val()=='') {
        $("#tel_code").focus();
      }else {
        $(".loading1").css("display","block");
        $(".mbtn").css("background","#fff");
        this.axios({
          method: 'post',
          url: SERVER+'traveler/alterTel',
          data: {
            newTel: $('#newTel').val(),
            oldTel: $('#oldTel').val(),
            verifyCode: $('#tel_code').val()
          },
          headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).then(function (res) {
          if(res.data.code == 0){
            alert(res.data.errorMsg);
            $(".iframe").css("display","none");
            $(".loading1").css("display","none");
            $(".mbtn").css("background","#769164");
          }else if (res.data.code == -1) {
            alert("系统异常，请稍后再试");
            $(".iframe").css("display","none");
            $(".loading1").css("display","none");
            $(".mbtn").css("background","#769164");
          }else if(res.data.code == 1){
            alert("修改成功");
            $(".iframe").css("display","none");
            $(".loading1").css("display","none");
            $(".mbtn").css("background","#769164");
            sessionStorage.setItem('user',JSON.stringify(res.data.loginedUser));
            that.msg.userTel=res.data.loginedUser.userTel;
          }
        }).catch(function (err) {
          alert("服务器出错了，请稍后再试");
          $(".iframe").css("display","none");
          $(".loading1").css("display","none");
          $(".mbtn").css("background","#769164");
        });
      }
    },

    // 修改密码
    //验证手机号
    phoneNumber:function(){
      let re=/^1[34578]\d{9}$/;
      let re2=/^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
      let phoneNumber=$('#phoneNumber').val();
      if ( re.test(phoneNumber) || re2.test(phoneNumber) ) {
        $('#numTishi').text("验证成功").css("color","#eee");
      }else{
        $('#numTishi').text("请输入正确的账号").css("color","#c97586");
      }
    },
    //验证密码
    pwd:function(){
      let re=/^[0-9A-Za-z]{8,16}$/;
      let pwd=$('#newPassword').val();
      if (pwd=='') {
        $('#pwdTishi').text("密码不能为空").css("color","#c97586");
      }else if ( re.test(pwd) ) {
        $('#pwdTishi').text("验证成功").css("color","#eee");
      }else{
        $('#pwdTishi').text("密码格式不正确").css("color","#c97586");
      }
    },
    //再次验证密码
    repwd:function(){
      let pwd=$('#newPassword').val();
      let repwd=$('#reNewPassword').val();
      if (repwd=='') {
        $('#repwdTishi').text("密码不能为空").css("color","#c97586");
      }else if ( pwd!=''&&pwd==repwd ) {
        $('#repwdTishi').text("验证成功").css("color","#eee");
      }else{
        $('#repwdTishi').text("两次输入密码不一致").css("color","#c97586");
      }
    },
    get_passwordCode(){
      let that=this;
      this.axios({
        method: 'post',
        url: SERVER+'traveler/sendVerifyCodeAction',
        data:{
          account: $("#myNum").val(),
          type: 3
        },
        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
      }).then(function (res) {
        if(res.data.code == 0){
          alert(res.data.errorMsg);
        }else if (res.data.code == -1) {
          alert("系统异常，请稍后再试");
        }else if(res.data.code == 1){
          that.sendCode();
        }
      }).catch(function (err) {
        alert("服务器出错了，请稍后再试");
      });
    },
    complete_password(){
      let that=this;
      if ($("#newPassword").val()=='') {
        $("#newPassword").focus();
      }else if ($("#reNewPassword").val()=='') {
        $("#reNewPassword").focus();
      }else if ($("#password_code").val()=='') {
        $("#password_code").focus();
      }else {
        $(".loading1").css("display","block");
        $(".mbtn").css("background","#fff");
        this.axios({
          method: 'post',
          url: SERVER+'traveler/alterPasswordAction',
          data: {
            account: $('#myNum').val(),
            userPassword: $('#newPassword').val(),
            userPassword2: $('#reNewPassword').val(),
            verifyCode: $('#password_code').val()
          },
          headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).then(function (res) {
          if(res.data.code == 0){
            alert(res.data.errorMsg);
            $(".iframe").css("display","none");
            $(".loading1").css("display","none");
            $(".mbtn").css("background","#769164");
          }else if (res.data.code == -1) {
            alert("系统异常，请稍后再试");
            $(".iframe").css("display","none");
            $(".loading1").css("display","none");
            $(".mbtn").css("background","#769164");
          }else if(res.data.code == 1){
            alert("修改成功");
            sessionStorage.removeItem('user');
            that.$router.push({path:'/login'});
            $(".iframe").css("display","none");
            $(".loading1").css("display","none");
            $(".mbtn").css("background","#769164");
          }
        }).catch(function (err) {
          alert("服务器出错了，请稍后再试");
          $(".iframe").css("display","none");
          $(".loading1").css("display","none");
          $(".mbtn").css("background","#769164");
        });
      }
    },

    // 绑定邮箱
    get_emailCode(){
      let that=this;
      this.axios({
        method: 'post',
        url: SERVER+'traveler/sendVerifyCodeAction',
        data: {
          account: $("#bindEmail").val(),
          type: 4
        },
        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
      }).then(function (res) {
        if(res.data.code == 0){
          alert(res.data.errorMsg);
        }else if (res.data.code == -1) {
          alert("系统异常，请稍后再试");
        }else if(res.data.code == 1){
          that.sendCode();
        }
      }).catch(function (err) {
        alert("服务器出错了，请稍后再试");
      });
    },
    complete_bindEmail(){
      let that=this;
      if ( $("#bindEmail").val()=="" ){$("#bindEmail").focus();}
      else if ( $("#email_code").val()=="" ) {$("#email_code").focus();}
      else {
        $(".loading1").css("display","block");
        $(".mbtn").css("background","#fff");
        this.axios({
          method: 'post',
          url: SERVER+'traveler/bindEmail',
          data: {
            account: $("#bindEmail").val(),
            verifyCode: $("#email_code").val()
          },
          headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).then(function (res) {
          if(res.data.code == 0){
            alert(res.data.msg);
            $(".iframe").css("display","none");
            $(".loading1").css("display","none");
            $(".mbtn").css("background","#769164");
          }else if (res.data.code == -1) {
            alert("系统异常，请稍后再试");
            $(".iframe").css("display","none");
            $(".loading1").css("display","none");
            $(".mbtn").css("background","#769164");
          }else if(res.data.code == 1){
            alert("绑定成功");
            $(".iframe").css("display","none");
            $(".loading1").css("display","none");
            $(".mbtn").css("background","#769164");
            sessionStorage.setItem('user',JSON.stringify(res.data.loginedUser));
            that.msg.userEmail=res.data.loginedUser.userEmail;
          }
        }).catch(function (err) {
          alert("服务器出错了，请稍后再试");
          $(".iframe").css("display","none");
          $(".loading1").css("display","none");
          $(".mbtn").css("background","#769164");
        });
      }
    },

    //完善信息
    // complete_addInfo(){
    //   let that=this;
    //   this.axios({
    //     method: 'post',
    //     url: '',
    //     data: {
    //       name: $('#myName').val(),
    //       id: $('#myId').val(),
    //       sex: $('input:radio[name="sex"]:checked').val()
    //     },
    //     headers: {'Content-Type': 'application/x-www-form-urlencoded'}
    //   }).then(function (res) {
    //     if(res.data.code == 0){
    //       alert(res.data.errorMsg);
    //     }else if (res.data.code == -1) {
    //       alert("系统异常，请稍后再试");
    //     }else if(res.data.code == 1){
    //       alert("完善成功");
    //       $(".iframe").css("display","none");
    //       // that.msg.userPassword=$("#reNewPassword").val();
    //     }
    //   }).catch(function (err) {
    //     alert("服务器出错了，请稍后再试");
    //   });
    // },

    // 查询已添加的乘客
    searchMan(){
      let that=this;
      this.axios({
        method: 'get',
        url: SERVER+'traveler/queryBuyer',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
      }).then(function (res) {
        if(res.data.code == 0){
          alert(res.data.msg);
        }else if (res.data.code == -1) {
          alert(res.data);
        }else if(res.data.code == 1){
          if (that.isLogin!=1) {alert(res.data.msg);}
          else if (res.data=="") {alert("还没有添加乘客");}
          that.mans=res.data.buyers;
        }
      }).catch(function (err) {
        alert("服务器出错了，请稍后再试");
      });
    },
    addMan(){
      $(".iframe").css("display","block");
      $("#addManBox").css("display","block");

      $("#iconBox").css("display","none");
      $("#usernameBox").css("display","none");
      $("#telBox").css("display","none");
      $("#passwordBox").css("display","none");
      $("#emailBox").css("display","none");
      $("#addInfoBox").css("display","none");

      $("#myName").val("");
      $("#myId").val("");
    },
    complete_addMan(){
      let that=this;
      if ($("#myName").val()=='') {
        $("#myName").focus();
      }else if ($("#myId").val()=='') {
        $("#myId").focus();
      }else {
        $(".loading2").css("display","block");
        $(".mbtn").css("background","#fff");
        this.axios({
          method: 'post',
          url: SERVER+'traveler/addBuyer',
          data: {
            buyerName: $("#myName").val(),
            buyerSex: $('input:radio[name="sex"]:checked').val(),
            idCard: $("#myId").val()
          },
          headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).then(function (res) {
          if(res.data.code == 0){
            alert(res.data.msg);
            $(".iframe").css("display","none");
            $(".loading2").css("display","none");
            $(".mbtn").css("background","#769164");
          }else if (res.data.code == -1) {
            alert("系统异常，请稍后再试");
            $(".iframe").css("display","none");
            $(".loading2").css("display","none");
            $(".mbtn").css("background","#769164");
          }else if(res.data.code == 1){
            if (that.isLogin!=1) {alert(res.data.msg);}
            alert("绑定成功");
            $(".iframe").css("display","none");
            $(".loading2").css("display","none");
            $(".mbtn").css("background","#769164");
            that.mans.push(res.data.buyer);
          }
        }).catch(function (err) {
          alert("服务器出错了，请稍后再试");
          $(".iframe").css("display","none");
          $(".loading2").css("display","none");
          $(".mbtn").css("background","#769164");
        });
      }
    },
    deletMan(id,index){
      let that=this;
      this.axios({
        method: 'post',
        url: SERVER+'traveler/deleteBuyer',
        data: {
          idCard: id
        },
        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
      }).then(function (res) {
        if(res.data.code == 0){
          alert(res.data.msg);
        }else if (res.data.code == -1) {
          alert("系统异常，请稍后再试");
        }else if(res.data.code == 1){
          if (that.isLogin!=1) {alert(res.data.msg);}
          alert("删除成功");
          that.mans.splice(that.mans[index]);
        }
      }).catch(function (err) {
        alert("服务器出错了，请稍后再试");
      });
    }
  }
}

//进入我的页面前，请求后端获取当前登陆用户数据

</script>

<style lang="css" scoped>
.gray{
  background: #bbb;
  color: #769164;
}
@media screen and (min-width: 768px){
  *{color: #fff;}
  /* 个人信息 */
  a{
    margin: 0 0 0 3px;
    font-size: 14px;
    color: #eee;
    text-decoration: none;
  }
  a:hover{
    color: #fff;
  }
  table{width: 80%;margin: 0 30px;position: relative;}
  tbody tr{
    border-bottom: 1px solid #eee;
    font-size: 15px;
  }
  .avatar{
    width: 100px;
    height: 100px;
    display: block;
  }
  .avatar img{
    width: 100%;
    height: 100%;
    border: 1px solid #ddd;
    border-radius: 50%;
  }
  .set_title{
    padding: 20px 0;
    width: 20%;
  }
  input{
    padding: 5px 10px;
    font-size: 15px;
    border: 1px solid #eee;
    border-radius: 4px;
    background-color: hsla(0,0%,71%,.1);
  }
  .btn,.addInfo{
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
  .btn:hover,.addInfo:hover{
    color: #eee;
    background: #42c02e;
    border: 1px solid #42c02e;
  }
  .addInfo{
    margin: 30px 0 60px;
  }
  .phoneNum{
    display: inline-block;
  }
  .form-group>input{width: 60%;}
  i{
    width: 20px;
    height: 20px;
    display: inline-block;
    margin: 0 0 0 10px;
    vertical-align: middle;
    background: url("../assets/img/icon/right.png");
    background-size: cover;
  }
  .num a{
    display: none;
  }
  .num:hover a{
    display: inline-block;
  }
  /* 订单 */
  .noDataImg{
    width: 460px;
    height: 345px;
    margin-left: 100px;
  }
  .noDataTxt{
    font-size: 25px;
    font-weight: bold;
  }
  /* 常用购票人 */
  .figure{
    width: 119px;
    padding: 10px;
    border-radius: 24px;
    box-shadow: 3px 3px 7px #a0a0a0;
    cursor: pointer;
    text-decoration: none;
    background: #eee;
  }
  .figure:hover{
    background: #fff;
  }
  .addImg{
    width: 25px;
    height: 25px;
    border-radius: 50%;
  }
  .addTxt{
    color: #769164;
    font-weight: bold;
  }
  .iframe{
    display: none;

    border-radius: 10px;
    padding: 30px;
    position: absolute;
    top: 15%;
    left: 10%;
    width: 80%;
    border-radius: 4px;
    z-index: 1;

    background-position: center top;
    background-size: cover;
    overflow: hidden;
  }
  .iframe:after {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      /* background-color: rgba(255,255,255,0.8); */
      z-index: -1;

      background-image: url('../assets/img/bg-pc.jpg');
      background-position: center top;
      background-size: cover;
      background-attachment: fixed;
      /* -webkit-filter: blur(5px);
      -moz-filter: blur(5px);
      -ms-filter: blur(5px);
      -o-filter: blur(5px); */
      filter: blur(5px);
      margin: -30px;
  }
  .iframe .closeImg{
    width: 24px;
    height: 24px;
    float: right;
  }
  .box{
    width: 200px;
    height: 200px;
    overflow: hidden;
  }
  .box>img{
    width: 200px;
    height: 200px;
  }
  #usernameBox{display: none;}
  #passwordBox{display: none;}
  #emailBox{display: none;}
  .mbtn{
    width: 60%;
    height: 31px;
    font-size: 16px;
    font-weight: bold;
    background: #eee;
    border: #eee;
    border-radius: 4px;
    color: #769164;
  }
  .mbtn:hover,.getCode:hover{
    background: #769164;
    border: #D56B60;
    color: #fff;
  }
  .buju{
    width: 60%;
    display: inline;
  }
  .form-group>span{
    margin: 0 10px;
    color: #eee;
    font-size: 15px;
  }
  /* 绑定邮箱 */
  .iframe > section{padding: 33px 0;}
  #emailBox > .form-group{
    width: 85%;
    margin: auto;
    padding: 12px 0;
  }
  .code{
    width: 60%;
    display: inline;
  }
  .getCode{
    width: 37%;
    height: 31px;
    float: right;
    background: #eee;
    color: #769164;
    border-radius: 4px;
    border: 1px solid #eee;
  }
}
</style>
