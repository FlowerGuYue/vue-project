<template lang="html">
  <section>
    <div class="info">
  		<ul>
  			<li>
  		    证件类型<input type="text">
  			</li>
  			<li>
  				证件号码<input type="number">
  			</li>
  			<li>
  				姓名<input type="number">
  			</li>
  			<li>
  				性别
  			</li>
  			<li>
  				手机号码<input type="number">
  			</li>
  			<li>
  				电子邮箱<input type="number">
  			</li>
  			<li>
  				旅客类型<input type="number">
  			</li>
  			<li class="confirm">
  				身份核验
  				<span class="pass">已通过</span>
  			</li>
  		</ul>
  		<ul style="display: none;">
  			<li>
  		    学校省份<input type="text">
  			</li>
  			<li>
  				学校<input type="number">
  			</li>
  			<li>
  				学制<input type="number">
  			</li>
  			<li>
  				入学年份
  			</li>
  		</ul>
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
.info .confirm{
  position: relative;
}
.info .pass{
  color: green;
  position: absolute;
  right: 20px;
}
</style>
