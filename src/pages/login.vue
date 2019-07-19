<template lang="html">
  <div class="bg">
    <div class="pc">
      <Header/>
      <Loginx :tabs="tabs">
        <!-- 密码登录 -->
        <template slot="tab1">
          <div class="form-group">
            <input type="text" class="form-control" id="account" placeholder="手机号/邮箱">
          </div>
          <div class="form-group">
            <input type="password" class="form-control" id="pwd" placeholder="密码">
          </div>
          <div class="form-group" style="position: relative">
            <img id="loading" class="loading" src="../assets/img/icon/loading (2).gif" alt="加载中……">
            <button class="btn" @click="pwdLogin">登录</button>
            <router-link to="/reg" class="reg">点击注册</router-link>
          </div>
        </template>
        <!-- 验证码登录 -->
        <template slot="tab2">
          <div class="form-group">
            <input type="text" class="form-control" id="account2" placeholder="手机号/邮箱">
          </div>
          <div class="form-group">
            <input type="text" class="form-control code" id="code" placeholder="验证码">
            <button class="getCode" v-bind:class="{gray:wait_timer>0}" @click="getCode">{{text()}}</button>
          </div>
          <div class="form-group" style="position: relative">
            <img id="loading" class="loading" src="../assets/img/icon/loading (2).gif" alt="加载中……">
            <button class="btn" @click="codeLogin">登录</button>
            <router-link to="/reg" class="reg">点击注册</router-link>
          </div>
        </template>
      </Loginx>
    </div>
    <div class="phone"></div>
  </div>
</template>

<script>
import {SERVER} from '@/config';
import Header from '@/components/header';
import Loginx from '@/components/loginx';

export default {
  name: 'Login',
  components: { Header,Loginx },
  data(){
    return {
      tabs: [
        {title: '密码登录', slotname: 'tab1'},
        {title: '验证码登录', slotname: 'tab2'}
      ],
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
    // 密码登录
    pwdLogin:function(){
      let that=this;
      if ($("#account").val()=='') {
        $("#account").focus();
      }else if ($("#pwd").val()=='') {
        $("#pwd").focus();
      }else {
        $(".loading").css("display","block");
        $(".btn").css("display","none");
        this.axios({
          method: 'post',
          url: SERVER+'traveler/loginByPwdService',
          data: {
            account: $("#account").val(),
            userPassword: $("#pwd").val()
          },
          headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        })
        .then(function (res) {
          sessionStorage.setItem('log',JSON.stringify(res.data.hasLoginedUser));
          if(res.data.code == 0){
            alert(res.data.msg);
            $(".loading").css("display","none");
            $(".btn").css("display","block");
          }else if (res.data.code == -1) {
            alert("系统繁忙，请稍后再试");
            $(".loading").css("display","none");
            $(".btn").css("display","block");
          }else if(res.data.code == 1){
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
          console.log(error);
          $(".loading").css("display","none");
          $(".btn").css("display","block");
        });
      }
    },
    // 验证码登录
    // 获得验证码
    getCode:function(){
      let that=this;
      this.axios({
        method: 'post',
        url: SERVER+'traveler/sendVerifyCodeAction',
        data: {
          account: $("#account2").val(),
          type: 1
        },
        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
      }).then(function (res) {
        if(res.data.code == 0){
          alert(res.data.msg);
        }else if (res.data.code == -1) {
          alert("系统繁忙，请稍后再试");
        }else if(res.data.code == 1){
          that.sendCode();
        }
      }).catch(function (error) {
        console.log(error);
      });
    },
    codeLogin:function(){
      let that=this;
      if ($("#account2").val()=='') {
        $("#account2").focus();
      }else if ($("#code").val()=='') {
        $("#code").focus();
      }else {
        $(".loading").css("display","block");
        $(".btn").css("display","none");
        this.axios({
          method: 'post',
          url: SERVER+'traveler/loginService',
          data: {
            account: $("#account2").val(),
            verifyCode: $("#code").val(),
          },
          headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        })
        .then(function (res) {
          sessionStorage.setItem('log',JSON.stringify(res.data.hasLoginedUser));
          if(res.data.code == 0){
            alert(res.data.msg);
            $(".loading").css("display","none");
            $(".btn").css("display","block");
          }else if (res.data.code == -1) {
            alert("系统繁忙，请稍后再试");
            $(".loading").css("display","none");
            $(".btn").css("display","block");
          }else if(res.data.code == 1){
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
          console.log(error);
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
@media screen and (min-width: 768px){
  .phone{
    display: none;
  }
  .bg {
    height: 100vh;
    background-image: url('../assets/img/bg-pc.jpg');
    background-size: cover;
    position: relative;
  }
  .code{
    width: 55%;
    display: inline;
  }
  .getCode{
    width: 40%;
    height: 31px;
    float: right;
    background: #eee;
    color: #769164;
    border-radius: 4px;
    border: 1px solid #eee;
  }
  .btn{
    width: 100%;
    font-size: 18px;
    font-weight: bold;
    background: #eee;
    border: #eee;
    color: #769164;
  }
  .btn:hover,.getCode:hover{
    background: #769164;
    border: #D56B60;
    color: #fff;
  }
  .reg{
    color: #eee;
    line-height: 40px;
    float: right;
  }
  .reg:hover{
    color: #fff;
  }
}
@media screen and (max-width: 767px){
  .pc{
    display: none;
  }
}
</style>
