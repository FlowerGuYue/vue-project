<template lang="html">
  <div class="container-fluid">
    <div class="row">
      <div class="col-lg-3">
        <ul id="pc">
          <li v-for="tab,index in tabs" :class="index==cur?'active':''" @click="cur=index">
            <!-- <span v-if="tab.slotname=='tab5'" @click="exit">{{tab.title}}</span>
            <span v-else>{{tab.title}}</span> -->
            <span>{{tab.title}}</span>
          </li>
        </ul>
        <ul id="phone">
          <li @click="perInfo()">个人信息</li>
          <li @click="book()">我的订单</li>
          <li @click="bookman()">常用购票人</li>
          <li @click="link()">联系客服</li>
          <li>退出登陆</li>
        </ul>
      </div>
      <div class="col-lg-9">
        <div v-if="this.isLogin!=1">
          <LoginNo/>
        </div>
        <div v-if="this.isLogin==1">
          <div v-for="tab,index in tabs" :style="{display: index==cur?'block':'none'}">
            <slot :name="tab.slotname"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {SERVER} from '@/config';
import LoginNo from '@/components/loginNo';

export default {
  props: ['tabs'],
  components: { LoginNo },
  data(){
    return {
      cur: 0,
      isLogin: '',
    }
  },
  created(){
    this.isLogin = sessionStorage.getItem('log');
  },
  methods: {
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
    perInfo:function(){this.$router.push({path:'/perInfo'})},
    book:function(){this.$router.push({path:'/book'})},
    bookman:function(){this.$router.push({path:'/bookman'})},
    link:function(){this.$router.push({path:'/link'})},
  }
}
</script>

<style lang="css" scoped>
ul{
  background: #f5f5f5;
  border-radius: 4px;
  width: 100%;
  padding: 16px 0;
}
li{
  list-style: none;
  width: 100%;
  text-align: center;
  line-height: 40px;
  color: #333;
  margin: 12px 0;
}
li:hover,.active{
  color: #fff;
  border-radius: 4px;
  background-color: #769164;
  cursor: pointer;
}
@media screen and (min-width: 768px){
  .container-fluid{
    padding-top: 90px;
  }
  .row{
    margin: 0 139px;
  }
  .col-lg-3{
    padding: 80px 60px 0;
  }
  #phone{display: none;}
  .col-lg-9{
    height: 497px;
    padding: 40px 60px 0;
  }
}
@media screen and (max-width: 767px){
  .container-fluid{
    padding-top: 71px;
  }
  #pc{display: none;}
  .col-lg-9{
    display: none;
  }
}
</style>
