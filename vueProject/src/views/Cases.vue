<template>
     <el-row>
      <el-col :span="3">
        <CaseList></CaseList>
      </el-col>
      <el-col :span="21">2</el-col>
  </el-row>
</template>

<script>
import CaseList from "@/components/CaseList";
export default {
  name: "Cases",
  components:{
    CaseList,
  }
}
</script>

<style scoped>

</style>