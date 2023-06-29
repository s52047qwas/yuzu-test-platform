<template>
  <div class="pro_list">
<!--    项目列表-->
    <div class="title">
      <span>项目列表</span>
      <el-button style="float: right" type="success" icon="el-icon-plus" @click="clickAdd">添加项目</el-button>
    </div>
    <div class="pro_table">
        <el-table :data="projectList" style="width: 100%">
        <el-table-column prop="name" label="项目名称" min-width="180" />
        <el-table-column prop="leader" label="负责人" min-width="180" />
        <el-table-column prop="desc" label="项目描述" min-width="180" show-overflow-tooltip/>
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
  </div>

  <!--  添加项目弹窗-->
  <el-dialog v-model="addDlg" title="添加项目" width="40%">
    <el-form :model="addForm">
      <el-form-item label="项目名称" >
        <el-input v-model="addForm.name" autocomplete="off"/>
      </el-form-item>
      <el-form-item label="项目描述" >
        <el-input v-model="addForm.desc" autocomplete="off"/>
      </el-form-item>

    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="addDlg = false">取消</el-button>
        <el-button type="primary" @click="addProject">
          确认
        </el-button>
      </span>
    </template>
  </el-dialog>

<!--  修改项目弹窗-->
  <el-dialog v-model="editDlg" title="编辑项目" width="40%">
    <el-form :model="editForm">
      <el-form-item label="项目名称">
        <el-input v-model="editForm.name" autocomplete="off"/>
      </el-form-item>
      <el-form-item label="项目描述">
        <el-input v-model="editForm.desc" autocomplete="off"/>
      </el-form-item>

    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="editDlg = false">取消</el-button>
        <el-button type="primary" @click="updateProject">
          确认
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script>
import { ElMessage, ElMessageBox } from 'element-plus'
import {mapMutations} from "vuex";

export default {
  name: "Project",
  data(){
    return {
      //项目列表数据
      projectList:[],
      //添加项目弹窗状态
      addDlg:false,
      addForm:{
        name:'',
        desc:''
      },
      editDlg:false,
      editForm:{
        name:'',
        desc:''
      }
    }
  },
  methods:{
    //获取项目列表信息
    ...mapMutations(['updateState']),
    async getAllProject(){
      const response = await this.$api.getProjects()
      if(response.status === 200){
        this.projectList = response.data
      }
    },
    //删除项目
    async delProject(id){
      const response = await this.$api.delProject(id)
      if(response.status === 204){
        ElMessage({
          type: 'success',
          message: '删除项目成功',
        })
        await this.getAllProject()
      }else{
        ElMessage({
          type: 'error',
          message: '删除项目异常',
        })
      }
    },
    //添加项目
    async addProject(){
      const response = await this.$api.addProject(this.addForm)
      if(response.status === 201){
        ElMessage({
          type: 'success',
          message: '添加项目成功',
        })
        await this.getAllProject()
        this.addDlg = false
      }else{
        ElMessage({
          type: 'error',
          message: '添加项目异常',
        })
      }
    },
    //修改项目
    async updateProject(){
      const response = await this.$api.updateProject(this.editForm.id,this.editForm)
      window.console.log(response.status)
      if(response.status === 200){
        ElMessage({
          type: 'success',
          message: '修改项目成功',
        })
        await this.getAllProject()
        this.editDlg = false
      }
    },
    //点击删除按钮
    clickDel(id){
      ElMessageBox.confirm(
        '确认是否删除该项目？',
        '提示',
        {
          confirmButtonText: '确认',
          cancelButtonText: '取消',
          type: 'warning',
        }
      )
      .then(() => {
        this.delProject(id)
      })
      .catch(() => {
        ElMessage({
          type: 'info',
          message: '取消删除项目',
        })
      })
    },
    //点击添加项目按钮
    clickAdd(){
      this.addDlg = true
      this.addForm = {name: '',desc:''}
    },
    //点击edit按钮
    clickEdit(info){
      this.editDlg = true
      this.editForm = {...info}
    },
    //点击detail按钮
    clickDetail(info){
      this.updateState({
        name:'pro',
        value:info
      })
      this.$router.push({name:'home2'})
    }
  },
  //页面初始化
  created() {
      this.getAllProject()
    }
}
</script>

<style scoped>
.pro_list{
  margin: 20px 100px 0 100px;
}
.title{
  height: 40px;
  color: #42b983;
  font: bold 16px/40px 微软雅黑;
  border-bottom: solid 3px #42b983;
}

</style>