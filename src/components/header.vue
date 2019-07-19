<template lang="html">
  <div class="hf">
    <!-- phone:头，pc：脚 -->
  	<header>想去哪就去哪~</header>
    <!-- 导航 -->
  	<footer id="pcFoot" v-if="reFresh">
      <div class="container-fluid">
        <img src="../assets/img/logo.png" alt="宏创" />
        <ul v-if="isRouterAlive" class="nav nav-pills">
          <li v-for="opt in opts">
            <div v-if="opt.id==3" @mouseover="dropShow" @mouseleave="dropHidden"><router-link :to="opt.to">{{opt.title}}</router-link></div>
            <div v-if="opt.id!=3"><router-link :to="opt.to">{{opt.title}}</router-link></div>
          </li>
          <div class="drop" v-show="ifShow" @mouseover="elOver" @mouseleave="elLeave">
            <p @click="friends('http://localhost:8080/#/','HC旅游','想去哪就去哪','http://47.110.225.74/userImg/logo.png')">邀请好友</p>
            <p v-if="this.isLogin!=1" @click="login">登陆</p>
            <p v-if="this.isLogin==1" @click="exit">退出登陆</p>
          </div>
        </ul>
      </div>
  	</footer>
  	<footer id="phoneFoot">
      <div class="col"><router-link to="/">首页</router-link></div>
      <div class="col"><router-link to="/rob">抢票</router-link></div>
      <div class="col"><router-link to="/trip">旅程</router-link></div>
      <div class="col"><router-link to="/mine">我的</router-link></div>
  	</footer>
  </div>
</template>

<script>
import {SERVER} from '@/config';
// import fImg from '../assets/img/logo.png';
export default {
  data(){
    return {
      opts: [
        {id: 0, title: '首页', isNew: true, to: '/'},
        {id: 1, title: '抢票', isNew: true, to: 'rob'},
        {id: 2, title: '旅程', isNew: true, to: 'trip'},
        {id: 3, title: '我的', isNew: true, to: 'mine'}
      ],
      cur:0,
      isLogin: '',
      reFresh: true,
      focused: false,
      ifShow: false,
      isRouterAlive: true
    }
  },
  updated(){
    this.isLogin = sessionStorage.getItem('log');
  },
  watch: {
    $route(to,from){
      this.reFresh=false;
      this.reFresh=true;
    }
  },
  methods: {
    dropShow(){
      this.ifShow = true;
    },
    dropHidden(){
      if (!this.focused)  this.ifShow = false;
      else  this.ifShow = true;
    },
    elOver(){
      this.ifShow = true;
      this.focused = true;
    },
    elLeave(){
      this.focused = false;
      this.ifShow = false;
    },
    // 邀请好友
    friends(url,title,summary,pics){
      var urlPath = "https://connect.qq.com/widget/shareqq/index.html?url="+ encodeURI(url) +
                    "&desc=&title=" + title +
                    "&summary=" + summary +
                    "&pics=" + pics;
      window.open (urlPath, 'qq分享', 'height=637, width=1053, top=195,left=459, toolbar=no, menubar=no, scrollbars=no, resizable=no,location=no, status=no');
    },
    // 去登录
    login(){
      this.$router.push({path:'/login'});
    },
    // 退出登陆
    exit(){
      let that=this;
      this.axios({
        method: 'post',
        url: SERVER+'traveler/loginOut',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
      }).then(function (res) {
        if (res.data.code == -1) {
          alert("系统异常，请稍后再试");
        }else if(res.data.code == 1){
          alert(res.data.msg);
          sessionStorage.removeItem('user');
          sessionStorage.setItem('log','0');
          that.$router.push({path:'/'});
        }
      }).catch(function (err) {
        console.log(err);
      });
    },
  }
}
</script>

<style lang="css" scoped>
/*pc端*/
@media screen and (min-width: 768px){
  .hf{
    position: fixed;
    z-index: 9999;
  }
  header{
    position: fixed;
    bottom: 0;
    width: 100%;
    height: 40px;
    line-height: 40px;
    text-align: center;
    background: transparent;
    color: #fff;
    font-family: 微软雅黑;
  }
  /* 导航栏 */
  #phoneFoot{display: none;}
  footer{
    position: fixed;
    top: 0;
    width: 100%;
    height: 10%;
    text-align: center;
    font-size:105%;
  }
  img{
    width: 100px;
    height: 50px;
    float: left;
    margin: 23px;
  }
  .nav{
    float: right;
    padding: 15px;
    position: relative;
  }
  .nav>li {
    width: 100px;
    height: 40px;
    line-height: 34px;
    margin: 12px;
    cursor: pointer;
    font-size: 18px;
    font-weight: bold;
  }
  .nav>li>div>a {
    text-decoration: none;
    width: 100%;
    height: 100%;
    display: inline-block;
    color: #fff;
    padding: 3px 10px;
    border-radius: 20px;
  }
  .nav>li>div>a:hover {
    color: #769164;
    background: #eee;
  }
  .router-link-exact-active{
    color: #769164 !important;
    background: #eee;
  }
  .drop{
    padding: 12px 8px 4px;
    background: #eee;
    color: #769164;
    border-radius: 3px;
    font-weight: 400;
    cursor: pointer;
    position: absolute;
    right: 37px;
    top: 67px;
  }
  .drop>p:hover{
    color: #555;
    text-decoration: underline;
  }
}
/*手机端*/
@media screen and (max-width: 767px){
  header{
    display: none;
    /* position: fixed;
    top: 0;
    width: 100%;
    height: 10%;
    line-height: 340%;
    text-align: center;
    font-size: 21px;
    color: #769164; */
  }
  #pcFoot{display: none;}
  footer{
    position: fixed;
    bottom: 0;
    width: 100%;
    height: 10%;
    line-height: 73px;
    text-align: center;
    font-size: 18px;
  }
  .col{
    display: inline-block;
    width: 82px;
  }
  .col > a{
    color: #769164;
    font-weight: bold;
  }
}
</style>
