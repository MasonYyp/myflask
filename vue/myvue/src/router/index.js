import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const Views = ()=>import("@/views")
const Login = ()=>import("@/views/Login")
const UserInfo = ()=>import("@/views/UserInfo")

const router = new VueRouter({
    routes:[
        {
            path:'/',
            // 一级导航
            component: Views,
            // 二级导航
            children:[
                {
                    // 重定向到login
                    path:'/',
                    redirect:'/login'
                },
                {
                    path:'/login',
                    name:'login',
                    component: Login,
                    meta:{
                        title:"登录"
                    }
                },
                {
                    path:'/userinfo',
                    name:'userinfo',
                    component: UserInfo,
                    meta:{
                        title:"用户信息"
                    }
                }
            ]
        }
    ]
});

// 设置页面标题
router.afterEach((to)=>{
    document.title = to.meta.title;
})

export default router;