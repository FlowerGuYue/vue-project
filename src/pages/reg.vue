<template lang="html">
  <section>
    <!-- <form v-if="cur_step==2" :action="SERVER+'api/reg'" ref="form3" method="post" enctype="multipart/form-data"> -->
    <div class="pc form-group" ref="reg_form">
      <div class="row">
        <div class="col-lg-12 reg-title">注册</div>
      </div>
      <div class="row">
        <div class="col-lg-3"><label for="phoneNumber">手机号：</label></div>
        <div class="col-lg-6">
          <input type="text" class="form-control" id="phoneNumber" @blur="phoneNumber">
        </div>
        <div class="col-lg-3 tishi" id="numTishi"></div>
      </div>
      <div class="row">
        <div class="col-lg-3"><label for="pwd">密码：</label></div>
        <div class="col-lg-6">
          <input type="password" class="form-control" id="pwd" @blur="pwd">
        </div>
        <div class="col-lg-3 tishi" id="pwdTishi">8-16位数字或字母</div>
      </div>
      <div class="row">
        <div class="col-lg-3"><label for="repwd">确认密码：</label></div>
        <div class="col-lg-6">
          <input type="password" class="form-control" id="repwd" @blur="repwd">
        </div>
        <div class="col-lg-3 tishi" id="repwdTishi"></div>
      </div>
      <div class="row">
        <div class="col-lg-3"><label for="code">验证码：</label></div>
        <div class="col-lg-6">
          <input type="text" class="form-control" id="code">
        </div>
        <div class="col-lg-3">
          <button class="getCode" v-bind:class="{gray:wait_timer>0}" @click="getCode">{{text()}}</button>
        </div>
      </div>
      <div class="row">
        <div class="col-lg-9" style="position: relative">
          <img id="loading" class="loading" src="../assets/img/icon/loading (2).gif" alt="加载中……">
          <button class="btn btn-default" @click="reg">注册</button>
        </div>
        <div class="col-lg-3">
          <router-link to="/login" class="login">立即登录</router-link>
        </div>
      </div>
    </div>
    <div class="phone form-group" style="position: relative">
      <div class="reg-title">注册</div>
      <input type="text" class="form-control" id="phoneNumber" @blur="phoneNumber" placeholder="手机号/邮箱">
      <p class="tishi" id="numTishi">手机号</p>
      <input type="password" class="form-control" id="pwd" @blur="pwd" placeholder="密码">
      <p class="tishi" id="pwdTishi">8-16位数字或字母</p>
      <input type="password" class="form-control" id="repwd" @blur="repwd" placeholder="确认密码">
      <p class="tishi" id="repwdTishi">再次输入密码</p>
      <div class="check-code">
        <input type="text" class="form-control code" id="code" placeholder="验证码">
        <button class="getCode" v-bind:class="{gray:wait_timer>0}" @click="getCode">{{text()}}</button>
      </div>
      <img id="loading" class="loading" src="../assets/img/icon/loading (2).gif" alt="加载中……">
      <div class="btn" @click="reg">注册</div>
      <router-link to="/login" class="login">立即登录</router-link>
    </div>
  </section>
</template>

<script>
import {SERVER} from '@/config';
export default {
  name: 'reg',
  data(){
    return{
      wait_timer:false
    }
  },
  methods: {
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
    //验证手机号
    phoneNumber:function(){
      let re=/^1[34578]\d{9}$/;
      let phoneNumber=$('#phoneNumber').val();
      if ( re.test(phoneNumber) ) {
        $('#numTishi').text("验证成功").css("color","#eee");
      }else{
        $('#numTishi').text("请输入正确的手机号").css("color","#c97586");
      }
    },
    //验证密码
    pwd:function(){
      let re=/^[0-9A-Za-z]{8,16}$/;
      let pwd=$('#pwd').val();
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
      let pwd=$('#pwd').val();
      let repwd=$('#repwd').val();
      if (repwd=='') {
        $('#repwdTishi').text("密码不能为空").css("color","#c97586");
      }else if ( pwd!=''&&pwd==repwd ) {
        $('#repwdTishi').text("验证成功").css("color","#eee");
      }else{
        $('#repwdTishi').text("两次输入密码不一致").css("color","#c97586");
      }
    },
    //获取验证码
    getCode:function(){
      let that=this;
      this.axios({
        method: 'post',
        url: SERVER+'traveler/sendVerifyCodeAction',
        data: {
          account: $("#phoneNumber").val(),
          type: 2
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
    // 注册
    reg:function(){
      let that=this;
      if ($("#phoneNumber").val()=='') {
        $("#phoneNumber").focus();
      }else if ($("#pwd").val()=='') {
        $("#pwd").focus();
      }else if ($("#repwd").val()=='') {
        $("#repwd").focus();
      }else if ($("#code").val()=='') {
        $("#code").focus();
      }else {
        $(".loading").css("display","block");
        $(".btn").css("display","none");
        this.axios({
          method: 'post',
          url: SERVER+'traveler/registAction',
          data: {
            userPassword: $("#pwd").val(),
            userPassword2: $("#repwd").val(),
            userTel: $("#phoneNumber").val(),
            verifyCode: $("#code").val()
          },
          headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        })
        .then(function (res) {
          if(res.data.code == 0){
            alert(data.msg);
            $(".loading").css("display","none");
            $(".btn").css("display","block");
          }else if (res.data.code == -1) {
            alert("系统繁忙，请稍后再试");
            $(".loading").css("display","none");
            $(".btn").css("display","block");
          }else if(res.data.code == 1){
            alert("注册成功");
            if (res.data.hasLoginedUser==1) {
              sessionStorage.setItem('user',JSON.stringify(res.data.loginedUser));
              that.$router.push({path:'/mine'});
              $(".loading").css("display","none");
              $(".btn").css("display","block");
            }else if (res.data.hasLoginedUser==0) {
              alert("系统繁忙，请稍后再试");
              $(".loading").css("display","none");
              $(".btn").css("display","block");
            }
          }
        }).catch(function (error) {
          alert("服务器出错了，请稍后再试");
          $(".loading").css("display","none");
          $(".btn").css("display","block");
        });
      }
    }
  }
}
</script>

<style lang="css" scoped>
.gray{
  background: #bbb;
  color: #769164;
}
@media screen and (min-width: 768px) {
  section{
    margin: auto;
    padding-top: 70px;
    width: 50%;
  }
  .phone{display: none;}
  .row{
    height: 60px;
    position: relative;
  }
  .reg-title{
    width: 100%;
    height: auto;
    line-height: 7px;
    text-align: center;
    font-size: 30px;
    color: #eee;
  }
  label{
    float: right;
    line-height: 34px;
    color: #eee;
    font-size: 16px;
  }
  .tishi{
    line-height: 30px;
    color: #eee;
    font-weight: bold;
    font-size: 15px
  }
  .getCode{
    border-radius: 4px;
    background: #eee;
    color: #769164;
    width: 91px;
    line-height: 30px;
    border: 1px solid #ccc;
  }
  .btn{
    width: 80%;
    float: right;
    font-size: 18px;
    font-weight: bold;
    background: #eee;
    border: #eee;
    color: #769164;
    margin-top: 20px;
  }
  .btn:hover,.getCode:hover{
    background: #769164;
    border: #769164;
    color: #fff;
  }
  .login{
    color: #eee;
    line-height: 75px;
    font-size: 17px;
  }
}
@media screen and (max-width: 767px){
  section{
    padding: 29px;
    height: 100vh;
    background-image: url("../assets/img/bg-phone.jpg");
    background-size: cover;
  }
  .pc{display: none;}
  .reg-title{
    width: 100%;
    height: 61px;
    text-align: center;
    font-size: 30px;
  }
  p{
    height: 28px;
    margin: 0 24px;
    color: #769164;
  }
  .form-control,.check-code{
    width: 90%;
    margin: auto;
    border-radius: 18px;
  }
  .code{
    width: 55%;
    float: left;
  }
  .getCode{
    border-radius: 4px;
    background: #fff;
    color: #555;
    width: 40%;
    height: 31px;
    float: right;
    border: 1px solid #ccc;
    border-radius: 18px;
  }
  .btn{
    width: 90%;
    margin: 24px 16px 0;
    background: #769164;
    border: #769164;
    color: #fff;
    border-radius: 18px;
  }
  .login{
    float: right;
    color: #769164;
    text-decoration: none;
    line-height: 40px;
    margin-right: 30px;
  }
}
</style>
