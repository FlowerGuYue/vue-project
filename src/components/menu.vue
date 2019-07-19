<template lang="html">
  <div class="container-fluid">
    <div class="row">
      <div class="col-lg-3">
        <ul id="pc">
          <li v-for="tab,index in tabs" :class="index==cur?'active':''" @click="cur=index">{{tab.title}}</li>
        </ul>
        <ul id="phone">
          <li @click="train()">火车</li>
          <li @click="airfly()">飞机</li>
          <li @click="ship()">轮船</li>
        </ul>
      </div>
      <div class="col-lg-9">
        <div v-for="tab,index in tabs" :style="{display: index==cur?'block':'none'}">
          <slot :name="tab.slotname"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['tabs'],
  data(){
    return {
      cur: 0
    }
  },
  methods: {
    train:function(){this.$router.push({path:'/perInfo'})},
    airfly:function(){this.$router.push({path:'/book'})},
    ship:function(){this.$router.push({path:'/bookman'})}
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
