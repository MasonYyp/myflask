<template>
  <div class="my_test">
    用户名：{{userName}}
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: 'Mytest',
  data: function(){
    return{
      userName:""
    }
  },

  mounted:function(){
    this.test()
  },

  methods:{
    test: function(){
      axios.post("/flask/userinfo/name").then(res=>{
        this.userName = res.data;
      });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
