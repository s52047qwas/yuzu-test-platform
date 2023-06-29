<template>
 <el-tabs type="border-card" style="height: calc(100vh - 60px)">
    <el-tab-pane label="项目模块"><modules></modules></el-tab-pane>
    <el-tab-pane label="测试任务">Config</el-tab-pane>
    <el-tab-pane label="环境管理">Role</el-tab-pane>
  </el-tabs>
</template>

<script>
import modules from "@/components/modules";

export default {
    components:{
      modules
    }
}
</script>

<style scoped>

</style>