<template>
  <div class="box">
    <div class="title">用例管理</div>

    <div class="case_list">
      <el-menu  default-active="2" class="el-menu-vertical-demo"
        style="background: none;border-right: 0"
        active-text-color="#ffd04b"
        text-color="black"
      >
        <el-submenu :index="task.id" v-for="task in tasks">
          <template #title>
            <span>{{ task.name }}</span>
          </template>
            <el-submenu :index="sui.name" v-for="sui in task.test_suits">
              <template #title>{{sui.name}}</template>
              <el-menu-item :index="testcase.title" v-for="testcase in sui.testcases">
                <el-tooltip class="box-item" effect="dark" :content="testcase.title" placement="right">
                  <span>{{testcase.title}}</span>
                </el-tooltip>
              </el-menu-item>

            </el-submenu>
        </el-submenu>
      </el-menu>
    </div>
  </div>
</template>

<script>
import {mapState} from "vuex";
export default {
  name: "CaseList",
  data(){
    return {
      tasks:[]
    }
  },
  methods:{
    ...mapState(['pro']),
    async getTasks(){
      const response = await this.$api.getTasks(this.pro.id)
      if(response.status === 200){
        this.tasks = response.data.results
      }
    }},
  created() {
    this.getTasks()
  }
}
</script>

<style scoped>
.title{
  font: bold 20px/40px 微软雅黑;
  text-align: center;
  border-bottom: solid 3px #42b983;
}
.box{
  height: calc(100vh - 56px);
  box-shadow: 0 0 5px #42b983;
  min-width: 150px;
}
</style>