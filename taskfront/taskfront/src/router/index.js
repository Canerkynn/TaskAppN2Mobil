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
