<template lang="html">
  <section>
    <div class="head">
  		<div class="top">
  			<a class="iconfont arrow" href="#">&#xe62c;</a>
  			<span>出发站</span>
  			<a href="#" class="ensure">确定</a>
  		</div>
  		<div class="inps">
  			<input type="text" autofocus  class="start">
  			<i class="icon"></i>
  			<input type="text" autofocus  class="end">
  		</div>
  	</div>
  	<div class="city">
  		<p>常用城市</p>
  		<div class="row always">
  			<div class="col-xs-4">北京</div>
  			<div class="col-xs-4">上海</div>
  			<div class="col-xs-4">上海</div>
  		</div>
  		<p>热门城市</p>
  		<div class="row hot">
  			<div class="col-xs-4">北京</div>
  			<div class="col-xs-4">上海</div>
  			<div class="col-xs-4">上海</div>
  		</div>
  		<div class="row hot">
  			<div class="col-xs-4">北京</div>
  			<div class="col-xs-4">上海</div>
  			<div class="col-xs-4">上海</div>
  		</div>
  		<div class="row hot">
  			<div class="col-xs-4">北京</div>
  			<div class="col-xs-4">上海</div>
  			<div class="col-xs-4">上海</div>
  		</div>
  	</div>
  </section>
</template>

<script>
export default {
}
</script>

<style lang="css" scoped>
a{
  text-decoration: none;
  color: #fff;
}
@font-face {
    /* font-family: Iconfont;
    src: url('fonts/iconfont.ttf'),
    url('fonts/iconfont.svg'),
    url('fonts/iconfont.eot'); */
  }
.iconfont {
    font-family:"iconfont" !important;
    font-size:18px;
    font-style:normal;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }
  .head{
    width: 100%;
    height: 100px;
    background:  #769164;
    position: relative;
  }
  .head .top{
    height: 40px;
    line-height: 40px;
    text-align: center;
    color: #fff;
  }
  .top .arrow{
    position: absolute;
    left: 10px;
    font-size: 25px;
    font-weight: lighter;
  }
  .top .ensure{
    position: absolute;
    right: 10px;
    font-size: 14px;
    font-weight: lighter;
  }
  .head .inps{
    padding:20px 20px;
    position: relative;
  }
  .inps input{
    border: 0;
    outline: 0;
    height: 30px;
    border-radius:2px;
  }
  .inps .start{
    width: 60%;
  }
  .inps .end{
    width:38%;
  }
  .inps .icon{
    /* background: url(img/delete.png); */
    width: 20px;
    height: 20px;
    position: absolute;
    top: 25px;
    right:45%;
    background-size: cover;
  }
  .city p{
    padding-left: 20px;
    line-height: 20px;
    margin:0;
  }
  .always,.hot{
    background: #fff;
    height: 45px;
    line-height: 45px;
    text-align: center;
  }
  .hot{
    border-bottom: 1px solid grey;
  }
</style>
