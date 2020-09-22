import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import ListTask from "../components/ListTask";
import TaskDetail from "../components/TaskDetail";
Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    },
    {
        path: '/listtask',
        name: 'ListTask',
        component: ListTask
    },
    {
        path: '/taskdetail',
        name: 'TaskDetail',
        component: TaskDetail
    },
]

const router = new VueRouter({
    routes
})

export default router
