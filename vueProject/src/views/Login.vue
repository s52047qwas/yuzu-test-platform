<template>
  <div class="login_bj">
    <div class="LoginBox">
        <div class="title">登 录 页 面</div>
        <el-form ref="loginRef" :model="form" :rules="rulesLogin" label-width="80px" :label-position="labelPosition">
          <el-form-item  label="账号" prop="name">
            <el-input v-model="form.name"></el-input>
          </el-form-item>

          <el-form-item label="密码" prop="pwd">
            <el-input v-model="form.pwd" type="password"></el-input>
          </el-form-item>

           <el-form-item label="记住账号">
            <el-switch v-model="form.status"></el-switch>
        </el-form-item>

      <el-form-item style="margin: auto;">
        <el-button type="primary" style="width: 50%" @click="clickLogin">登录</el-button>
        <el-button>注册</el-button>
      </el-form-item>
      </el-form>
    </div>
  </div>

</template>

<script>
import { ElMessage } from 'element-plus'
import {mapMutations} from "vuex";

  export default {
    methods:{
      ...mapMutations(['updateState']),
      //登录点击时间，规则校验，然后调用登录接口
      clickLogin(){
        this.$refs.loginRef.validate((res) =>{
          if(res){
            this.loginSet()
          }
        })
      },
      //调用登录接口
      async loginSet(){
          const params = {
            username : this.form.name,
            password : this.form.pwd,
          }
          const response = await this.$api.login(params)
          //获取token
          const token = response.data.token

          //判断是否登录成功
          if(response.status===200){
                //跳转到project页面（编程式导航）
                this.$router.push('/project')
                ElMessage.success('登录成功！')
                //将token存储
                // window.sessionStorage.setItem('token', token)  //将token存储到sessionStorage
                window.localStorage.setItem('token', token)   //将token存储到localStorage
                this.updateState({
                  name:'isAuthenticated',
                  value: true
                })
                window.localStorage.setItem('username',this.form.name)

                //判断是否记住账号，如果记住，则保存到localstorage
                if(this.form.status){
                      const userInfo = JSON.stringify(this.form)
                      window.localStorage.setItem('userInfo',userInfo)
                }else{
                      //如果没记住，则清空userInfo
                      window.localStorage.removeItem('userInfo')
                }

          }else{
            ElMessage.error('账号或密码错误！')
          }

      }
    },
    data(){
      return {
        labelPosition: 'right',
        //账号密码，记住用户默认数据
        form:{
          name:'',
          pwd:'',
          status: false
        },
        rulesLogin:{
          //输入框规则校验
          name:[
              { required: true, message: 'Please input User name', trigger: 'blur' }
          ],
          pwd:[
              { required: true, message: 'Please input password', trigger: 'blur' },
              { min: 6, max: 8, message: 'Length should be 6 to 8', trigger: 'blur' },
          ]
        }
      }
    },
    created() {
      //判断是否存在用户，如果有则填充到账号密码处
      const userInfo = window.localStorage.getItem('userInfo')
      if(userInfo){
        this.form = JSON.parse(userInfo)
      }
    }
  }

</script>

<!--//scoped 表示样式只对当前组件有效-->
<style scoped>
  .el-form-item__label{
    /* 调整element自带内容的眼神，需要用important提示权重 */
    color: white !important;
  }

  .login_bj{
    height: 100vh;
    background: url("../assets/image/login_bh.jpg");
    background-size: cover;
  }
  .LoginBox{
    width: 600px;
    height: 350px;
    /*margin: 200px auto;  !*居中*!*/
    /* 通过定位让盒子居中 */
    position: relative;
    top: calc(50vh - 300px);
    left: calc(50vw - 300px);

    box-shadow: 0 0 5px salmon;   /*阴影*/
    padding: 20px;  /* 内边距 */
    border-radius: 10px;  /*边框*/
    background: darkturquoise;
  }
  .title{
    height: 60px;
    font: bold 24px/60px "微软雅黑";
    color: white;
    text-align: center;
    padding-bottom: 30px;
  }

</style>