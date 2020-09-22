<template>
    <div class="">
        <div class="row">
            <div class="col-md-5 text-center taskDetails">
                <h3 style="color:blue;" class="mb-5">Task Detail </h3>

                <p class="mb-3">Title : {{taskdetail.title}}</p>

                <p class="mb-3">Description: {{taskdetail.description}}</p>


                <p class="mb-3">Label : {{taskdetail.label}}</p>

                <p class="mb-3 " style="color:red">Employee : {{taskdetail.employee}}</p>

                <p v-if="taskdetail.status == 'todo' ">
                    <label for="employee" >Another Employee: </label>
                    <select class="ml-2" name="employee" id="employee" v-model="employee">
                        <option v-for="employee in employees" v-if="employee.username != taskdetail.employee" selected="selected"> {{employee.username}}  </option>
                    </select>
                </p>

                <p class="mb-3">Status : {{taskdetail.status}}</p>

                <p class="mb-3" style="color:orange"> Author : {{taskdetail.author}}</p>


                <p class="mb-3" style="color:orange"> P_Date : {{taskdetail.publish_date}}</p>



                <footer class="card-footer" v-if="this.taskdetail.status != 'done'">
                    <a class="card-footer-item" v-on:click="setStatus(taskdetail.id, 'done',) ">Done</a>
                </footer>
                <footer class="card-footer" v-if="this.taskdetail.status != 'todo'">
                    <a class="card-footer-item" v-on:click="setStatus(taskdetail.id, 'todo') ">Todo</a>
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
                    console.log(res.data)
                    this.taskdetail.status = status
                    this.logout();
                    this.$router.push('/listtask');
                    // this.$router.push('/listtask', ).catch(()=>{});
                })
            },
            idFind_employee(){
                for (let i = 0; i<this.users.length;i++){
                    console.log(this.employee)
                    console.log(this.users[i]);
                    if (this.users[i].username == this.employee || this.users[i].username == this.author){
                        this.employee = this.users[i].id;
                        break;
                    }
                }
                console.log(this.employee)
                return this.employee
            },
            idFind_author(employee){

                for (let i = 0; i<this.users.length;i++){
                    console.log("author",employee)
                    if (this.users[i].username == employee){
                        console.log("author",this.employee)
                        this.author = this.users[i].id;
                        console.log("author_sayi",this.author)
                        break;
                    }
                }
                return this.author
            },
            getUsers() {
                axios.get("http://127.0.0.1:8000/api/users/")
                    .then(res => {
                        this.users = res.data;
                        console.log(res.data);
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
                .then(res => (this.employees =res.data)) //console.log(res.data)
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
        margin-top: 10%;
    }
</style>