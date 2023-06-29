import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import installElementPlus from './plugins/element'
import api from "@/api";
import tools from "@/assets/js/tools";
//引入自定义的全局css
import './assets/css/main.css'


const app = createApp(App)

//导入element-plus的图标
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

installElementPlus(app)
app.config.globalProperties.$api = api
app.config.globalProperties.$tools = tools

app.use(store).use(router).mount('#app')