<template>
    <div class="" v-if="taskdetail">
        <div class="row">
            <div class="col-md-12 text-center taskDetails">
                <h1 class="mb-5">{{taskdetail.title}}</h1>

                <p class="mb-3" v-html="taskdetail.description"> {{taskdetail.description}}</p>

                <table class="table table-bordered ">
                    <thead>
                    <tr>
                        <th scope="col" class="text-capitalize">Author</th>
                        <th scope="col" class="text-capitalize">Label</th>
                        <th scope="col" class="text-capitalize">Employee</th>
                        <th scope="col" class="text-capitalize">Published Date</th>
                        <th scope="col" class="text-capitalize" v-if="taskdetail.status == 'done' ">Another Employee</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <th scope="row">{{taskdetail.author}}</th>
                        <th scope="row">{{taskdetail.label}}</th>
                        <th scope="row">{{taskdetail.employee}}</th>
                        <th scope="row">{{taskdetail.publish_date.slice(0,10)}}</th>
                        <th scope="row" v-if="taskdetail.status == 'done' ">
                            <select class="ml-2" name="employee" id="employee" v-model="employee">
                                <option v-for="employee in employees" selected="selected" v-if="employee.username != taskdetail.employee">
                                    {{employee.username}}
                                </option>
                            </select>
                        </th>
                    </tr>
                    </tbody>
                </table>
                <footer class="card-footer btn-status"  v-if="this.taskdetail.status != 'todo'">
                    <a class="card-footer-item " type="button" v-on:click="setStatus(taskdetail.id, 'todo',) ">Todo</a>
                </footer>
                <footer class="card-footer btn-status-2" v-if="this.taskdetail.status != 'done'">
                    <a class="card-footer-item" type="button" v-on:click="setStatus(taskdetail.id, 'done') ">done</a>
                </footer>
                <footer class="card-footer" >
                    <a class="card-footer-item " type="button" v-on:click="deleteTask(taskdetail.id) ">Delete Task</a>
                </footer>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "TaskDetails",
        components: {
        },
        props:{
            taskdetail: {},
        },
        data() {
            return {
                employees: {},
                employee: null,
                publish_date: new Date(),
                title:null,
                users: [],
            }
        },
        methods: {
            setStatus(task_id, status){
                axios({
                    method:'put',
                    url:'http://127.0.0.1:8000/api/tasks/'+ task_id + '/',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    data: {
                        title:this.taskdetail.title,
                        description:this.taskdetail.description,
                        label:this.taskdetail.label,
                        status:status,
                        employee: this.idFind_employee() || this.taskdetail.employee,
                        author:this.idFind_author(this.taskdetail.employee) || this.idFind_author(this.taskdetail.author),
                        publish_date:new Date(),
                    },

                }).then(res => {
                    this.taskdetail.status = status

                })
            },
            idFind_employee(){
                for (let i = 0; i<this.users.length;i++){
                    if (this.users[i].username == this.employee || this.users[i].username == this.author){
                        this.employee = this.users[i].id;
                        break;
                    }
                }
                return this.employee
            },
            idFind_author(employee){

                for (let i = 0; i<this.users.length;i++){
                    if (this.users[i].username == employee){
                        this.author = this.users[i].id;
                        break;
                    }
                }
                return this.author
            },
            getUsers() {
                axios.get("http://127.0.0.1:8000/api/users/")
                    .then(res => {
                        this.users = res.data;
                    })
                    .catch(err => console.log(err));
            },
            logout() {
                localStorage.removeItem('user-token');
                this.token =  null;
                this.username = "";
                this.password = "";
            },

        },
        created() {
            axios.get("http://127.0.0.1:8000/api/users/")
                .then(res => (this.employees =res.data))
                .catch(err => console.log(err));
            this.getUsers();

        }
    }
</script>

<style scoped>
    .taskDetails {
        float: left;
        text-align: center;
        width:100%;
        margin-top: 2%;
    }
    .btn-status {
        color: #fff !important;
        text-transform: uppercase;
        text-decoration: none;
        background: #ed3330;
        padding: 20px;
        border-radius: 5px;
        display: inline-block;
        border: none;
        transition: all 0.4s ease 0s;
    }
    .btn-status-2 {
        color: #fff !important;
        text-transform: uppercase;
        text-decoration: none;
        background: #42b983;
        padding: 20px;
        border-radius: 5px;
        display: inline-block;
        border: none;
        transition: all 0.4s ease 0s;
    }
    .btn-status:hover {
        background: #42b983;
        letter-spacing: 1px;
        -webkit-box-shadow: 0px 5px 40px -10px rgba(0,0,0,0.57);
        -moz-box-shadow: 0px 5px 40px -10px rgba(0,0,0,0.57);
        box-shadow: 5px 40px -10px rgba(0,0,0,0.57);
        transition: all 0.4s ease 0s;
    }
    .btn-status-2:hover {
        background: #ed3330;
        letter-spacing: 1px;
        -webkit-box-shadow: 0px 5px 40px -10px rgba(0,0,0,0.57);
        -moz-box-shadow: 0px 5px 40px -10px rgba(0,0,0,0.57);
        box-shadow: 5px 40px -10px rgba(0,0,0,0.57);
        transition: all 0.4s ease 0s;
    }

</style>