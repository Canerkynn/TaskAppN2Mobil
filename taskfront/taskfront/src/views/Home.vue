<template>
    <div class="">
        <div id="nav" class="nav2">
            <b-navbar toggleable="lg" type="dark" variant="info">
                <b-navbar-brand href="#">Task APP</b-navbar-brand>
                <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            </b-navbar>
        </div>

        <div class="form-group register">

            <h3>User Registration</h3>
            <form class="form-group  mt-3 " @submit.prevent="CreateUser" >
                <p>
                    <input class="text-center" type="text" name="username" id="username" v-model="username" placeholder="USERNAME">
                </p>
                <p>
                    <input class="description text-center" type="password" name="password" id="password" v-model="password" placeholder="PASSWORD">
                </p>
                <input class="btn-info " type="submit" v-if="username || password == !null" value="Sign Up">
            </form>
            <div class="button">
                <button class="btn-block btn-danger" @click="loginPage">Login Page</button>
            </div>
        </div>
    </div>

</template>

<script>
    import axios from 'axios';
    export default {
        name: "home",
        components: {

        },
        data(){
            return {
                username: null,
                password:null,
            }
        },
        methods: {
            CreateUser() {
                axios.post('http://127.0.0.1:8000/api/users/ ', {
                    username: this.username,
                    password: this.password,
                })
                    .then(res => console.log(res))
                    .catch(err => console.log(err))
                this.$router.push('/listtask').catch(()=> {});
                this.username = "";
                this.password = "";
            },
            loginPage(){
                this.$router.push('/listtask').catch(()=>{});
            },

        }
    }
</script>
<style>
    .register {
        width: 40%;
        margin-left:30%;
        text-align: center;
        margin-top: 10%;
    }
    .button {
        width: 200px;
        border: orange 3px solid;
        margin:auto;
        margin-top: 50%;
    }
</style>
