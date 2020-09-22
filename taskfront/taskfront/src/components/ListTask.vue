<template>
    <div class="listtask" >
        <div id="nav" class="nav2">
            <b-navbar toggleable="lg" type="dark" variant="info">
                <b-navbar-brand href="#">Task APP</b-navbar-brand>
                <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
                <b-navbar-nav class="ml-auto">
                    <b-nav-form @submit.prevent="logout" v-if="token !== null">
                        <b-button size="sm" class="my-2 my-sm-0" type="submit">Logout</b-button>
                    </b-nav-form>
                    <b-nav-form @submit.prevent="register" v-if="token == null">
                        <b-button size="sm" class="my-2 my-sm-0" type="submit">Register</b-button>
                    </b-nav-form>
                </b-navbar-nav>
            </b-navbar>
        </div>
        <div v-if="token == null"><!--Giriş yapıp görevlerin sıralandığı yer burası -->
            <h2 class="titleh2"> Login User</h2>
            <p>
                <input class="text-center" type="text" name="username" id="username" v-model="username" placeholder="Username">
            </p>
            <p>
                <input class="text-center" type="password" name="password" id="password" v-model="password" placeholder="Password">
            </p>
            <p>
                <input  type="submit" value="Submit" @click="login()">
            </p>
        </div>
        <div class="row" v-if="token !== null">
            <div class="col-md-12 text-center nicefont">
                <h4 style="margin-right:7% "> Welcome to Task App {{this.username}}</h4>
                <form @submit="createdNew()" style="margin-right:7% ">
                    <input class="btn-sm btn-primary mb-3 btn-center" type="submit" id="createNew"  value="Create new task" >
                </form>
                <div class="col-md-12 mb-5 mt-5" style="margin-left: 20%;" v-if="createNew">
                    <div class="col-md-6"><!--bu kısım butona basıp görev oluşturduğumuz kısım-->
                        <div class="card">
                            <div class="card-body">
                                <form id="formtask" @submit.prevent="checkForm('todo',username)">
                                    <div class="input-group mb-3">
                                        <div class="input-group-prepend">
                                            <span class="input-group-text"  for="title">Title</span>
                                        </div>
                                        <input type="text" name="title" id="title" v-model="title" class="form-control" aria-label="Default" aria-describedby="inputGroup-sizing-default">
                                    </div>
                                    <div class="input-group mb-3">
                                        <div class="input-group-prepend">
                                            <span class="input-group-text" for="description">Description</span>
                                        </div>
                                        <input type="text" name="description" id="description" v-model="description" class="form-control" aria-label="Default" aria-describedby="inputGroup-sizing-default">
                                    </div>
                                    <div class="input-group mb-3">
                                        <div class="input-group-prepend">
                                            <span class="input-group-text " for="label">Label</span>
                                        </div>
                                        <input type="text" name="label" id="label" v-model="label" class="form-control" aria-label="Default" aria-describedby="inputGroup-sizing-default">
                                    </div>
                                    <div class="input-group mb-3">
                                        <div class="input-group-prepend">
                                            <label class="input-group-text" for="employee">Employee</label>
                                        </div>
                                        <select class="custom-select" name="employee" id="employee" v-model="employee">
                                            <option v-for="employee in users" selected="selected"> {{employee.username}} </option>
                                        </select>
                                    </div>
                                    <button type="submit" value="Submit"  class="btn btn-primary btn-lg btn-block">Kaydet</button>

                                </form>
                            </div>
                        </div>
                    </div>
                </div>
                <!--<div class=" col-md-6 task_square">
                    <h2 style="color:red;"> DONE</h2>
                    <h3  v-bind:key="task.id" :tasks="tasks" v-for="task in tasks" v-if="task.status=='done'">
                        {{task.title}}
                        <br>
                        <small >Description{{tasks.description}}</small>
                        <br>
                        <button class="btn-sm btn-primary mt-2 mb-3" v-on:click="taskDetail(task)"> Details </button>
                        <hr>
                    </h3>
                </div>
                <div class="col-md-6 task_square">
                    <h2 style="color:red;"> TODO </h2>
                    <h3  v-bind:key="task.id" :tasks="tasks" v-for="task in tasks" v-if="task.status=='todo'">
                        {{task.title}}
                        <br>
                        <small >Description{{tasks.description}}</small>
                        <br>
                        <button class="btn-sm btn-primary mt-2 mb-3" v-on:click="taskDetail(task)"> Details </button>
                        <hr/>
                    </h3>
                </div>
            </div>
        </div>
        <div class="row details" v-if="token !== null">
            <div class=" col-md-12  " >
                <TaskDetails v-bind:taskdetail="taskdetail"></TaskDetails>
            </div>
        </div>-->
                <div class="table-responsive" style="width: 90%;">
                    <table class="table table-bordered " >
                        <thead>
                        <tr>
                            <th scope="col" class="text-danger">Id</th>
                            <th scope="col" class="text-danger">Title</th>
                            <th scope="col" class="text-danger">Author</th>
                            <th scope="col" class="text-danger">DESC</th>
                            <th scope="col" class="text-danger">Label</th>
                            <th scope="col" class="text-danger">Employee</th>
                            <th scope="col" class="text-danger">Published Date</th>
                            <th scope="col" class="text-danger">Status</th>
                            <th scope="col" class="text-danger">Detail</th>
                        </tr>
                        </thead>
                        <tbody>
                        {{this.emp}}asdasd
                        <tr  v-bind:key="task.id" :tasks="tasks" v-for="(task) in tasks" v-if="task.employee == username">
                            <th scope="row">{{task.id}}</th>
                            <th scope="row">{{task.title}}</th>
                            <th scope="row">{{task.author}}</th>
                            <th scope="row">{{task.description}}</th>
                            <th scope="row">{{task.label}}</th>
                            <th scope="row">{{task.employee}}</th>
                            <th scope="row">{{task.publish_date}}</th>
                            <th scope="row" v-if="task.status == 'done'"><span class="badge badge-pill badge-success">{{task.status}}</span></th>
                            <th scope="row" v-if="task.status == 'todo'"><span class="badge badge-pill badge-danger">{{task.status}}</span></th>
                            <button class="button btn-info mt-2 mb-3" v-on:click="taskDetail(task)"> Details </button>
                        </tr>
                        </tbody>
                    </table>
                </div>
                <div class="details">
                    <TaskDetail v-bind:taskdetail="taskdetail"></TaskDetail>
                </div>
            </div>
        </div>

        <!-- <script type="text/x-template" id="modal-template">
             <transition name="modal">
                 <div class="modal-mask">
                     <div class="modal-wrapper">
                         <div class="modal-container">

                             <div class="modal-header">
                                 <slot name="header">
                                     Task Detail
                                 </slot>
                             </div>

                             <div class="modal-body">
                                 <slot name="body">
                                     default body
                                 </slot>
                             </div>

                             <div class="modal-footer">
                                 <slot name="footer">
                                     default footer
                                     <button class="modal-default-button" @click="$emit('close')">
                                         OK
                                     </button>
                                 </slot>
                             </div>
                         </div>
                     </div>
                 </div>
             </transition>
         </script>-->
    </div>
</template>

<script>
    import axios from 'axios';
    import TaskDetail from "./TaskDetail";
    //import TaskDetails from "./TaskDetails";
    //import CreateTask from "./CreateTask";
    export default {
        name: "ListTask",
        components: {
            TaskDetail,
        },
        data() {
            return {
                tasks: [],
                taskdetail: Object,
                author: '',
                createNew: "",
                token:localStorage.getItem('user-token') || null,
                username: '',
                password: '',
                users: [],
                title:'',
                description:'',
                label:'',
                employee:'',
                emp: '',
            }
        },
        methods: {
            login() {
                axios.post('http://127.0.0.1:8000/auth/', {
                    username: this.username,
                    password: this.password,
                })
                    .then(resp => {
                        this.token = resp.data.token;
                        console.log(resp);
                        localStorage.setItem('user-token', resp.data.token);
                    })
                    .catch(err => {
                        localStorage.removeItem('user-token')
                    })
                console.log("1.", this.username);
                this.emp = this.username;
            },
            getTasks() {
                axios.get("http://127.0.0.1:8000/api/tasks/")
                    .then(res => {
                        this.tasks = res.data;
                        this.getUsers(this.tasks);
                    })
                    .catch(err => console.log(err));
            },
            logout() {
                localStorage.removeItem('user-token');
                this.token =  null;
                this.username = "";
                this.password = "";
            },
            register(){
                this.$router.push('/').catch(()=>{});
            },
            getUsers(tasks) {
                axios.get("http://127.0.0.1:8000/api/users/")
                    .then(res => {
                        this.users = res.data;
                        for(let i = 0; i<this.users.length;i++){
                            for(let j=0; j<tasks.length;j++){
                                if(tasks[j].author == this.users[i].id){
                                    tasks[j].author = this.users[i].username;
                                }
                                if(tasks[j].employee == this.users[i].id){
                                    this.emp = tasks[j].author;
                                    tasks[j].employee = this.users[i].username;

                                }
                            }
                        }
                    })
                    .catch(err => console.log(err));
            },
            checkForm(status,username) {
                axios({
                    method:'post',
                    url:'http://127.0.0.1:8000/api/tasks/',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    data: {
                        title: this.title,
                        description: this.description,
                        author:this.compare(username),
                        label: this.label,
                        status:status,
                        employee:this.idFind(),
                        publish_date:new Date(),
                    }
                }).then(res => {
                    console.log(res.data);
                    console.log(res.data.title,res.data.description,res.data.label,res.data.employee,res.data.status,res.data.author,res.data.publish_date)
                    this.compare(username);
                    this.logout();
                    this.res="";
                    this.createdNew();
                }).catch(err => console.log(err))

            },
            createdNew(){
                this.createNew = !this.createNew;
            },
            compare(username){
                for(let i=0;i<this.users.length;i++){
                    console.log("emp",this.users[i]);
                    console.log("username",this.users[i].username);
                    console.log("userrrname",username);
                    if(this.users[i].username == username){
                        console.log(this.username);
                        console.log(this.users[i]);
                        return this.users[i].id
                    }
                }

            },
            idFind(){
                for (let i = 0; i<this.users.length;i++){
                    console.log(this.employee)
                    console.log(this.users[i]);
                    if (this.users[i].username == this.employee){
                        this.employee = this.users[i].id;
                        break;
                    }
                }
                console.log(this.employee)
                return this.employee
            },
            taskDetail(task) {
                this.taskdetail = task;
            },

        },
        created() {
            createNew:false;
            token:localStorage.getItem('user-token')
            this.getTasks();

        }
    }

</script>

<style scoped>
    .nicefont {
        float: left;
        text-size:26px;
        text-align: left;
        margin-left: 5%;
        width: 20%;
    }
    .listtask {
        margin-top:5%;
    }
    .titleh2 {
        margin-bottom: 3%;
    }
    .nav2 {
        margin-top: -5%;
    }
    .details{
        margin-left: 35%;
        margin-bottom:5%;
        width: 50%;
        font-size: 24px;

    }
</style>