import { createRouter, createWebHashHistory } from 'vue-router'
import Login from "@/views/Login";
import Home from "@/views/Home";
// import Project from "@/views/Project";
import Cases from "@/views/Cases";
import Data from "@/views/project";
import Plan from "@/views/Plan";
import store from "@/store/index";

const routes = [
    //路由重定向
    {
        path: "/",
        redirect: "/login"
    },
    {
        path: "/login",
        component:Login,
        name:'login'
    },
    {
            path: "/project",
            //路由懒加载模式
            component:() => import("@/views/AllProject"),
            name:'pro'
    },
    {
        path: "/home",
        component:Home,
        name:'home',
        children:[
            {
                path:"/case",
                component:Cases,
                name:'cases'
            },
            {
                path:"/env",
                component:() => import("@/views/env"),
                name:'env'
            },
            {
                path:"/interface",
                component:() => import("@/views/interface"),
                name:'interface'
            },
             {
                path:"/pro",
                component:() => import("@/views/project"),
                name:'project'
            }
        ]
    },
        {
        path: "/home2",
        //路由懒加载模式
        component:() => import("@/views/Home2"),
        name:'home2',
        children: [
            {
                path:"/case",
                component:Cases,
                name:'cases'
            },
            {
                path:"/env",
                component:() => import("@/views/env"),
                name:'env'
            },
            {
                path:"/interface",
                component:() => import("@/views/interface"),
                name:'interface'
            },
             {
                path:"/pro",
                component:() => import("@/views/project"),
                name:'project'
            }
        ]
    }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  // const isAuthenticated = window.localStorage.getItem('token')
  const isAuthenticated = store.state.isAuthenticated
  if (to.name !== 'login' && !isAuthenticated) next({ name: 'login' })
  else next()
})

export default router
