<template lang="html">
  <div>
    <section>
      <img src="../assets/img/idea.png" alt="未登录">
      <p>
        正在开发中，敬请期待！
        <!-- <router-link to="/index" class="goto">去查询出行计划</router-link> -->
      </p>
    </section>
  </div>
</template>

<script>

export default {
  name: 'trip',
  components: {  }
}
</script>

<style lang="css" scoped>
img{
  width: 300px;
  height: 300px;
  display: block;
  margin: auto;
}
p{
  width: 180px;
  height: 20px;
  font-size: 16px;
  margin: auto;
  color: #eee;
}
.goto{
  width: auto;
  color: #eee;
  font-size: 18px;
}
@media screen and (min-width: 768px){
  section{
    padding-top: 116px;
  }
  .noLogin{
    display: none;
  }
}
@media screen and (max-width: 767px){
  section{
    padding-top: 71px;
  }
  .noLogin{
    display: none;
  }
}
</style>
