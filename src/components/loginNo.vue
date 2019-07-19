<template lang="html">
  <div>
    <img src="../assets/img/noLogin.png" alt="未登录">
    <p>
      还没登录呢~
      <router-link to="/login" class="login">立即登录</router-link>
    </p>
  </div>
</template>

<script>
export default {
}
</script>

<style lang="css" scoped>
div{
  padding-top: 70px;
}
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
.login{
  width: auto;
  color: #eee;
  font-size: 18px;
}
</style>
