import axios from "axios";
import {h} from "vue";


//创建一个请求对象
// eslint-disable-next-line no-unused-vars
const http = axios.create({
    baseURL: 'http://127.0.0.1:8090',
    // eslint-disable-next-line no-unused-vars
    validateStatus: function (status) {
        return true}
});


//设置请求拦截器
http.interceptors.request.use(function (config) {
    // 在发送请求之前做些什么
    //接口鉴权
    //判断是否登录和注册接口, 如果是则不处理
    if(config.url === '/user/login/' || config.url === '/user/register/') return config
    const token = window.localStorage.getItem('token')  //获取存储的token数据
    config.headers.Authorization = 'Bearer ' + token
    return config
  });


//封装接口请求方法
export default {
    //登录请求
    login(params){
        return http.post('/user/login/',params)
    },
    //注册请求
    register(params){
        return http.post('/user/register/', params)
    },
    //获取项目列表
    getProjects(){
        return http.get('/projects/')
    },
    //删除项目
    delProject(id){
        return http.delete(`/projects/${id}`)
    },
    //添加项目
    addProject(params){
        return http.post('/projects/',params)
    },
    //修改项目
    updateProject(id,params){
        return http.patch(`/projects/${id}/`,params)
    },
    //全局公共属性获取，环境数据
    //环境信息
    getEnvs(project_id){
        return http.get('/environment/',{
            params:{
                project:project_id
            }
        })
    },
    //测试用例
    getTasks(project_id){
        return http.get('/task/',{
             params:{
                project:project_id
            }
        })
    },
    //获取模块
    getModule(project_id){
        return http.get('/modules/',{
                params:{
                project:project_id
            }
        })
    },
    //接口相关
    getInterface(){
        return http.get('/interface/')
    },
    setInterface(params){
        return http.post('/interface/',params)
    }
}

