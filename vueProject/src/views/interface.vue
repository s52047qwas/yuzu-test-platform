<template>
  <div class="box">
    <el-button style="float: left;margin-bottom: 10px" type="success" icon="el-icon-plus" @click="clickAdd">添加接口</el-button>
<!--     <el-scrollbar max-height="calc(100vh - 110px)">-->
        <el-table :data="interface" style="width: 100%" height="calc(100vh - 115px)" size="mini" border>
        <el-table-column prop="name" label="接口名称" min-width="180" />
        <el-table-column prop="url" label="接口地址" min-width="180" />
        <el-table-column prop="developer" label="所属开发人员" min-width="180" />
        <el-table-column prop="module" label="所属模块" min-width="180" />
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
<!--     </el-scrollbar>-->
    </div>
</template>

<script>
export default {
  name: "interface",
  data(){
    return {
      interface:[]
    }
  },
  methods:{
    async getInterface(){
      const response = await this.$api.getInterface()
      if(response.status===200){
        this.interface = response.data
      }
    }
  },
  created() {
    this.getInterface()
  }
}
</script>

<style scoped>
.box{
  padding: 10px;
}

</style>