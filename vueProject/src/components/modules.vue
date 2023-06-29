<template>
  <div class="title">
      <el-button style="float: left" type="success" icon="el-icon-plus" @click="clickAdd">添加模块</el-button>
    </div>
  <div class="pro_table">
        <el-table :data="modules" style="width: 100%">
        <el-table-column prop="name" label="模块名称" min-width="180" />
       <el-table-column label="接口数量" min-width="180">
          <template #default="scope">
            {{scope.row.interfaces.length}}
          </template>
        </el-table-column>
          <el-table-column label="创建时间" min-width="180">
            <template #default="scope">
              {{$tools.rTime(scope.row.c_time)}}
            </template>
          </el-table-column>
        <el-table-column prop="address" label="操作" min-width="280">
          <template #default="scope">
            <el-button link @click="clickDetail(scope.row)" type="primary" size="small" icon="el-icon-view">Detail</el-button>
            <el-button link @click="clickEdit(scope.row)" type="primary" size="small" icon="el-icon-edit">Edit</el-button>
            <el-button link @click="clickDel(scope.row.id)" type="danger" size="small" icon="el-icon-delete">Delete</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
</template>

<script>
import {mapState} from "vuex";

export default {
  name: "modules",
  data(){
    return {
      modules:[]
    }
  },
  computed:{
    ...mapState(['pro'])
  },
  methods:{
    async getModule(){
      const response = await this.$api.getModule(this.pro.id)
      if(response.status===200){
        this.modules = response.data
      }
    }
  },
  created() {
    this.getModule()
  }
}
</script>

<style scoped>
.title{
  min-width: 100px;
  height: 40px;
  color: #42b983;
  font: bold 16px/40px 微软雅黑;
  border-bottom: solid 1px blue;
}

</style>