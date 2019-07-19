<template lang="html">
  <section>
    <div class="info">
  		<ul>
  			<li>
  				<label for="mail">电子邮箱</label>
  				<input type="email" placeholder="请输入常用邮箱" name="mail">
  			</li>
  			<li>
  				<label for="mobile">手机号码</label>
  				<input type="number" name="mobile">
  			</li>
  			<li>
  				<label for="pwd">密 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;码</label>
  				<input type="password" name="pwd" style="position: relative;">
  				<a href="#" class="edit">修改密码</a>
  			</li>
  		</ul>
  		<router-link to="/addInfo">完善信息</router-link>
  		<span>如需获得更多功能请完善信息</span>
  	</div>
  </section>
</template>

<script>
export default {
}
</script>

<style lang="css" scoped>
section{
  padding-top: 58px;
}
.info{
  width: 100%;
  margin-top: 10px;
}
.info ul li{
   width: 100%;
   height: 40px;
   border-bottom: 1px solid #f8f8f8;
   background: #fff;
   padding:0 20px;
   line-height: 40px;
   position: relative;
}

.info ul li input{
  outline: 0;
  border: 0;
  height: 39px;
  text-indent: 3px;
  position: absolute;
  right: 0;
  width: 78%;
}
.edit{
  display: inline-block;
  width: 80px;
  height: 30px;
  border: 0;
  background:  #769164;
  border-radius: 5px;
  position: absolute;
  right: 10px;
  top: 5px;
}
.info a{
  display: inline-block;
  width: 80px;
  height: 30px;
  border: 0;
  background:  #769164;
  border-radius: 5px;
  margin-left: 30px;
  color: #fff;
  line-height: 30px;
  text-align: center;
}
.info a:focus,a:hover{
  text-decoration: none;
}
.info span{
  font-size: 12px;
  padding-left: 10px;
}
</style>
