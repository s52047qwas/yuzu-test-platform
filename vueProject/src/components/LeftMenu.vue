<template>
  <div class="menu_box">
    <!-- 用户信息-->
    <div class="user_box">
      <img src="../assets/image/logo.png" class="logo">
      <div class="user_info">
        <el-dropdown trigger="click" @command="handleCommand">
          <span class="el-dropdown-link" style="color:black;">
            <el-icon><UserFilled /></el-icon>
            {{ username }}
            <el-icon class="el-icon--right"><CaretBottom/></el-icon>
          </span>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item command="selectPro">项目选择</el-dropdown-item>
              <el-dropdown-item command="logout">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </div>
    </div>
    <div class="menu_tags">
    <!-- 菜单列表-->
      <el-menu router default-active="2" class="el-menu-vertical-demo"
        style="background: none;border-right: 0"
        active-text-color="#ffd04b"
        text-color="black"
      >
        <el-menu-item :index="itme.path" v-for="itme in menuList">
          <span :class="itme.icon"></span>
          <span>{{itme.name}}</span>
        </el-menu-item>
      </el-menu>
    </div>

  </div>
</template>

<script>
import menus from "@/components/menu";
import {mapMutations} from "vuex";

export default {
  name: "LeftMenu",
  data(){
    return{
      menuList:menus
    }
  },
  computed:{
    username(){
      return window.localStorage.getItem('username')
    }
  },
  methods:{
    ...mapMutations(['updateState']),
    handleCommand(command){
      if(command==='selectPro'){
        this.$router.push({name:'pro'})
      }else if(command==='logout'){
        window.localStorage.removeItem('token')
        this.$router.push({name:'login'})
        this.updateState({
          name:'isAuthenticated',
          value: false
        })
      }
    }
  }
}
</script>

<style scoped>
.user_box {
  height: 53px;
  /*边框*/
  border-bottom: solid 1px #ffffff;
  /*平行*/
  display: flex;
  /*  居中*/
  align-items: center;
}

.logo {
  width: 32px;
  height: 32px;
  /*图片变成圆形*/
  border-radius: 50px;
  /*左边距*/
  /*padding-left: 10px;*/
  background: white;
  margin: 0 20px;
}
/*菜单栏颜色*/
.el-menu-item:focus{
  background: black;
}
.el-menu-item:hover{
  background: #42b983;
}
</style>