<template>
  <div id="app">
    <div v-if="$route.name=='reg'">
      <router-view/>
    </div>
    <div v-if="$route.name!='reg'">
      <Header/>
      <router-view/>
    </div>
  </div>
</template>

<script>
import Header from '@/components/header';

export default {
  name: 'App',
  components: { Header }
}
</script>

<style>
@media screen and (min-width: 768px){
  #app{
    background-repeat: no-repeat;
    background-size: cover;
    overflow: hidden;
  }
  #app:after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: -1;
    background: url("./assets/img/bg-pc.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center center;
    filter: blur(8px);
  }
}
@media screen and (max-width: 767px){
  #app{
  }
}
</style>
