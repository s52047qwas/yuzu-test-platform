<template>
  <h1>环境管理</h1>
</template>

<script>
import {mapState,mapMutations,mapActions,mapGetters} from "vuex"
export default {
  name: "env",
  computed:{
    ...mapState(['name','age','envs']),
    ...mapGetters(['age2'])
  },
  methods:{
    ...mapMutations(['updateName','updateEnv']),
    ...mapActions(['getALLEnv'])
  },
  created() {
    this.getALLEnv(2)
  }
}
</script>

<style scoped>

</style>