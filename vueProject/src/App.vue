<template>
<!--  访问对应的路由路径，对应组件将渲染在router-view标签中-->
  <router-view></router-view>

</template>

<script>

export default {
  name: 'App',
  components: {
  },
  //解决vuex在刷新页面时数据丢失的问题
  created() {
    //页面刷新时，将vuex的数据保存到sessionStorage
    window.addEventListener('beforeunload', () => {
      sessionStorage.setItem('messageStore',JSON.stringify(this.$store.state));
    });
    //页面加载时读取sessionStorage数据
    sessionStorage.getItem('messageStore') && this.$store.replaceState(Object.assign(
        this.$store.state,JSON.parse(sessionStorage.getItem('messageStore'))));
  }
}
</script>

<style>

</style>
