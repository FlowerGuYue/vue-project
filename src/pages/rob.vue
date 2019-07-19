<template lang="html">
  <Menu :tabs="tabs">
    <template slot="tab1">
      <figure>
        <img class="noDataImg" src="../assets/img/无数据.png" alt="">
        <span class="noDataTxt">还没有订单哦~</span>
      </figure>
      <!-- 订单列表 -->
      <ol>
        <li></li>
      </ol>
    </template>
    <template slot="tab2">
      <figure>
        <img class="noDataImg" src="../assets/img/无数据.png" alt="">
        <span class="noDataTxt">还没有订单哦~</span>
      </figure>
      <!-- 订单列表 -->
      <ol>
        <li></li>
      </ol>
    </template>
    <template slot="tab3">
      <figure>
        <img class="noDataImg" src="../assets/img/无数据.png" alt="">
        <span class="noDataTxt">还没有订单哦~</span>
      </figure>
      <!-- 订单列表 -->
      <ol>
        <li></li>
      </ol>
    </template>
  </Menu>
</template>

<script>
import Menu from '@/components/menu';

export default {
  name: 'rob',
  components: { Menu },
  data(){
    return {
      tabs: [
        {title: '火车', slotname: 'tab1'},
        {title: '飞机', slotname: 'tab2'},
        {title: '轮船', slotname: 'tab3'}
      ]
    }
  }
}
</script>

<style lang="css" scoped>
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
ul{
  padding-top: 40px;
}
li{
  list-style: none;
}
@media screen and (min-width: 768px){
  section{
    padding-top: 116px;
  }
  .row{
    margin: 0 139px;
  }
  .noDataImg{
    width: 460px;
    height: 345px;
    margin-left: 10%;
  }
  .noDataTxt{
    font-size: 25px;
    font-weight: bold;
  }
}
@media screen and (max-width: 767px){
  section{
    padding-top: 71px;
  }
  .figure{
    position: relative;
    bottom: -154px;
    left: 117px;
  }
  figure{
    display: none;
  }
}
</style>
