import { createStore } from 'vuex'
import api from "@/api/index";

export default createStore({
  //全局公共数据
  state: {
    name:"yuzu",
    age:18,
    envs:[],
    pro:null,
    isAuthenticated:false
  },
  //全局公共计算属性
  getters: {
    age2(state){
      return state.age * 10
    }
  },
  //全局方法，对数据更新
  mutations: {
    updateName(state,value){
      state.name = value
    },
    updateEnv(state,value){
      state.envs = value
    },
    updateState(state,item){
      state[item.name] = item.value
      window.console.log(item.name,item.value)
    }
  },
  //全局异步方法，接口请求
  actions: {
    async getALLEnv(context, project_id){
      const response = await api.getEnvs(project_id)
      //context.commit进行数据修改提交
      context.commit('updateEnv', response.data)
    }
  },
  modules: {
  }
})
