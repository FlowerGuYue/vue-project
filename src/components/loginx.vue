<template lang="html">
  <section>
    <ul>
      <li v-for="tab,index in tabs" :class="index==cur?'active':''" @click="cur=index">{{tab.title}}</li>
    </ul>
    <div v-for="tab,index in tabs" :style="{display: index==cur?'block':'none'}">
      <slot :name="tab.slotname"/>
    </div>
  </section>
</template>

<script>
export default {
  props: ['tabs'],
  data(){
    return {
      cur: 0
    }
  }
}
</script>

<style lang="css" scoped>
section{
  width: 30%;
  position: absolute;
  top: 140px;
  left: 520px;
  padding: 29px;
  border-radius: 4px;
  z-index: 1;

  background-position: center top;
  background-size: cover;
  overflow: hidden;
}
section:after {
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
li{
  list-style: none;
  float: left;
  width: 50%;
  text-align: center;
  padding: 10px;
  border-radius: 5px;
  color: #eaedf7;
  font-size: 18px;
  font-weight: bold;
  cursor: pointer;
  margin-bottom: 27px;
}
li:hover,.active{
  color: #eee;
  border-bottom: 2px solid #eee;
}
</style>
