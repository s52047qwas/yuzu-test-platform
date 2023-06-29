<template>
  <div class="home_box">
    <div class="left_box">
      <leftMenu></leftMenu>
    </div>

    <div class="right_box">
      <div class="tag_box">
        <Tags></Tags>
      </div>
      <el-card class="main_box" body-style="padding: 0px">
        <router-view></router-view>
      </el-card>
    </div>
  </div>

</template>

<script>
import leftMenu from "@/components/LeftMenu";
import Tags from "@/components/Tags";

export default {
  components:{
    leftMenu,
    Tags
  }
}
</script>

<style scoped>
  .home_box{
    height: 100vh;
    background-image: linear-gradient(#0f7eec, #4248b9);
    display: flex;
  }
  .left_box{
    width: 200px;
    border-right: solid 1px #ffffff;
  }
  .right_box{
    height: 100vh;
    flex: 1;
  }
  .tag_box{
    height: 50px;
    background: white;
    margin: 2px;
  }
  .main_box{
    background: white;
    margin: 0 2px;
    height: calc(100vh - 60px);
  }
</style>