<template>
  <el-menu class="el-menu-demo" mode="horizontal">
    <el-menu-item index="1">
      <router-link :to="{name:'data'}">项目面板</router-link>
      </el-menu-item>
    <el-menu-item index="2">
      <router-link :to="{name:'plan'}">测试计划</router-link>
      </el-menu-item>
    <el-menu-item index="3" >
      <router-link :to="{name:'cases'}">测试用例</router-link>
      </el-menu-item>
  </el-menu>

  <router-view></router-view>

<!--    <h1>Home页面</h1>-->
<!--    <router-link to="/login">登录页面</router-link>-->
<!--    <hr>-->
<!--&lt;!&ndash;   命名路由&ndash;&gt;-->
<!--    <router-link :to="{name:'pro'}">Project页面</router-link>-->

</template>

<script>
export default {
  name: "Home"
}
</script>

<style scoped>

</style>