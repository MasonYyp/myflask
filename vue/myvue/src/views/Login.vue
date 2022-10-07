<template>
  <div class="login">
    <div>Login</div>
    <div class="lo_cont">
      <div>
        用户名：<el-input v-model="name" placeholder="请输入用户名"></el-input>
      </div>
      
      <div>
        密码：<el-input v-model="pwd" placeholder="请输入密码" show-password></el-input>
      </div>
      
      <div>
        验证码：<img v-bind:src="codeImgSrc"><el-input v-model="code" placeholder="请输入验证码"></el-input>
      </div>
      <el-button v-on:click="login">提交</el-button>
    </div>
  
  </div>
</template>

<script>

import axios from 'axios'

// 按需引入ElementUI组件
import 'element-ui/lib/theme-chalk/index.css' 
import { Input, Button, Message } from 'element-ui'


export default {
  name: 'Login',
  props: {
    msg: String
  },
  components:{
    elInput: Input,
    elButton: Button
  },

  data:function(){
    return{
      name:"mason",
      pwd:"123456",
      code:"",
      codeKey: "",
      codeImgSrc: ""
    }
  },

  created:function(){
    this.get_captcha()
  },

  methods:{

    get_captcha: function(){
      axios.post("/flask/public/captcha").then(res=>{
        console.log("login")
        console.log(res)
        console.log(res.data)
        console.log("login")
        let data = res.data.data;
        this.codeImgSrc = data.code_img;
        this.codeKey = data.code_key;
      })
    },

    login: function(){
      let param = {
        name: this.name,
        pwd: this.pwd,
        code_key: this.codeKey,
        code: this.code
      }

      // 使用json方式传参
      axios.post("/flask/public/login", param).then(res=>{
        let data = res.data;
        console.log(data)
        if(data.code == 1){
          localStorage.setItem("token", data.data.token);
          localStorage.setItem("retoken", data.data.retoken);
          Message.success("登录成功");
          location.href = "/#/userinfo";
        }
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.lo_cont>>>.el-input{
  width: 30%;
}

</style>
