<template>
    <div class="login-tasklist">
        <div id="nav">
            <b-navbar toggleable="lg" type="dark" variant="light" style="background-color: transparent;">
                <b-navbar-brand href="#">Task APP</b-navbar-brand>
                <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
                <b-navbar-nav class="ml-auto">
                    <b-nav-form @submit.prevent="logout" v-if="token !== null">
                        <b-button size="sm" class="btn btn-danger my-2 my-sm-0" type="submit">Logout</b-button>
                    </b-nav-form>
                    <b-nav-form @submit.prevent="register" v-if="token == null">
                        <b-button size="sm" class="my-2 my-sm-0" type="submit">Register</b-button>
                    </b-nav-form>
                </b-navbar-nav>
            </b-navbar>
        </div>

        <div class="container" v-if="token == null">
            <div class="row register-page">
                <div class="col-lg-4 col-md-6 col-sm-8 mx-auto"  >
                    <div style="background-color: bisque" class="card login" >
                        <h1>Sign In</h1>
                        <form class="form-group" @submit.prevent="login" >
                            <input class="form-control" type="text" name="username" id="username" v-model="username" placeholder="Username" required>
                            <input class="form-control" type="password" name="password" id="password" v-model="password" placeholder="Password" required>
                            <input class="btn btn-block btn-dark " type="submit" value="Sign In">
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <div class="row table-striped tbl" v-if="token !== null">
            <div class=" card col-md-9  text-center nicefont" style="background-color: antiquewhite; ">
                <h4 > Welcome to Task App </h4>
                <form @submit="createdNew()" style=" float:left;">
                    <input class="btn-sm btn-primary btn-block mb-3 btn-center" type="submit" id="createNew"  value="Create new task" >
                </form>

                <div class="col-md-12 mb-5 mt-5" style="margin-left: 25%;" v-if="createNew">
                    <div class="col-md-6">
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
                                            <div>
                                                <quill-editor
                                                        type="text" name="description" id="description" v-model="description"
                                                        ref="myQuillEditor"
                                                        :options="editorOption"
                                                /></div>
                                        </div>
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
                                    <button type="submit" value="Submit"  class="btn btn-primary btn-lg btn-block">Save</button>

                                </form>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="table-responsive " style="width: 80%; margin:auto;" v-if="!hideDetail && !createNew">
                    <table class="table table-bordered ">
                        <thead>
                        <tr>
                            <th scope="col" class="text-danger">Title</th>
                            <th scope="col" class="text-danger">Author</th>
                            <th scope="col" class="text-danger">DESC</th>
                            <th scope="col" class="text-danger">Label</th>
                            <th scope="col" class="text-danger">Employee</th>
                            <th scope="col" class="text-danger">Published Date</th>
                            <th scope="col" class="text-danger">Status</th>
                            <th scope="col" class="text-danger">Detail</th>
                            <th scope="col" class="text-danger">Delete</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr  v-bind:key="task.id" :tasks="tasks" v-for="(task) in tasks" v-if="task.employee == username">
                            <th scope="row">{{task.title}}</th>
                            <th scope="row">{{task.author}}</th>
                            <th scope="row" v-html="task.description.slice(0,10)"> </th>
                            <th scope="row">{{task.label}}</th>
                            <th scope="row">{{task.employee}}</th>
                            <th scope="row">{{task.publish_date.slice(0,10)}}</th>
                            <th scope="row" v-if="task.status == 'done'"><span class="badge badge-pill badge-success">{{task.status}}</span></th>
                            <th scope="row" v-if="task.status == 'todo'"><span class="badge badge-pill badge-danger">{{task.status}}</span></th>
                            <th scope="row"><button class="btn-warning " v-on:click="taskDetail(task)"> Details </button></th>
                            <th scope="row"><button class="btn-dark" v-on:click="deleteTask(task.id)"> Delete </button></th>
                        </tr>
                        </tbody>
                    </table>
                </div>

                <div style=" margin:auto;" v-if="hideDetail && !createNew">
                    <div v-if="taskdetail !== null" >
                        <TaskDetail v-bind:taskdetail="taskdetail"></TaskDetail>
                    </div>
                </div>
                <form class="mt-5" @submit="closeDetail()" v-if="hideDetail && !createNew" >
                    <input class="btn-sm btn-danger btn-block mb-3 btn-center" type="submit" id="hideDetail"  value="Close Detail" >
                </form>
            </div>

        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import TaskDetail from "./TaskDetail"
    import { quillEditor } from 'vue-quill-editor'
    export default {
        name: "ListTask",
        components: {
            TaskDetail,
            quillEditor,
        },
        data() {
            return {
                tasks: [],
                taskdetail:  Object,
                author: this.author,
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
                hideDetail:'',
                content:'',
                editorOption: {
                    placeholder:'Your Description',
                    readOnly:true,
                    theme: 'snow',
                    modules: {
                        toolbar:{

                        }
                    }
                },
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
                        localStorage.setItem('user-token', resp.data.token);
                    })
                    .catch(err => {
                        localStorage.removeItem('user-token')
                        this.$alert("Username or Password wrong")
                    })
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
                    method: 'post',
                    url: 'http://127.0.0.1:8000/api/tasks/',
                    data: {
                        title: this.title,
                        description: this.description,
                        author: this.compare(username),
                        label: this.label,
                        status: status,
                        employee: this.idFind(),
                        publish_date: new Date(),
                    }
                }).then(res => {
                    let newTask ={
                        'title': this.title,
                        'description': this.description,
                        'author': this.compare(username),
                        'label': this.label,
                        'status': status,
                        'employee': this.idFind(),
                        'publish_date': new Date(),
                    }
                    this.tasks.push(newTask);
                    this.getTasks();
                    this.createdNew();
                })
                    .catch(err => console.log(err))
            },
            createdNew(){
                this.createNew = !this.createNew;
                this.title ="";
                this.description="";
                this.label="";
                this.getTasks();

            },
            deleteTask(id){
                 axios({
                    method:'delete',
                    url:'http://127.0.0.1:8000/api/tasks/'+ id + '/',
                    headers: {
                        'Content-Type': 'application/json',
                    },

                }).then(res => {
                    this.getTasks();
                 })
            },
            compare(username){
                for(let i=0;i<this.users.length;i++){
                    if(this.users[i].username == username){
                        return this.users[i].id
                    }
                }

            },
            idFind(){
                for (let i = 0; i<this.users.length;i++){
                    if (this.users[i].username == this.employee){
                        this.employee = this.users[i].id;
                        break;
                    }
                }
                return this.employee
            },
            taskDetail(task) {
                this.taskdetail = task;
                this.hideDetail = true;
            },
            closeDetail(){
                this.hideDetail=false;
                this.taskdetail=null;
            }

        },
        created() {
            createNew:true;
            token:localStorage.getItem('user-token')
            this.getTasks();
            this.author = this.author;
            this.employee = this.employee;
            this.password = this.password;
            this.taskdetail = null;
            this.hideDetail = false;
        }
    }

</script>

<style scoped>
    @import "~vue2-editor/dist/vue2-editor.css";
    @import '~quill/dist/quill.core.css';
    @import '~quill/dist/quill.bubble.css';
    @import '~quill/dist/quill.snow.css';
    .login-tasklist{
        background: url(https://images.pexels.com/photos/533671/pexels-photo-533671.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)
        no-repeat center center;
        background-size: cover;
        height: 100%;
        position: absolute;
        width: 100%;
        z-index: -1;
    }
    .nicefont {
        float: left;
        text-size:26px;
        text-align: left;
        margin-left: 5%;
        width: 20%;
    }
    .card {
        padding: 20px;
    }
    .form-group input {
        margin-bottom: 20px;
    }
    .register-page {
        align-items: center;
        display: flex;
        height: 70vh;
    }
    .tbl {
        margin-left:12%;
        width: 88%;
    }
</style>