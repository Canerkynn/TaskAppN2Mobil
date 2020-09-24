<template>
    <div class="">
        <div class="register-page">
            <div class="wallpaper-register"></div>
            <div class="container">
                <div class="row">
                    <div class="col-lg-4 col-md-6 col-sm-8 mx-auto">
                        <div style="background-color: bisque" class="card login">
                            <h1>Sign Up</h1>
                            <form class="form-group" @submit.prevent="CreateUser" >
                                <input class="form-control" type="text" name="username" id="username" v-model="username" placeholder="Username" required>
                                <input class="form-control" type="password" name="password" id="password" v-model="password" placeholder="Password" required>
                                <input class="btn btn-block btn-dark " type="submit" value="Sign Up">
                            </form>
                        </div>
                    </div>
                </div>
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
                }).then(res => {
                    this.username = "";
                    this.password = "";
                    this.$router.push('/listtask');
                }).catch(err => {this.$alert('Already user exists ')})

            },
        }
    }
</script>
<style>
    .card {
        padding: 20px;
    }
    .form-group input {
        margin-bottom: 20px;
    }
    .register-page {
        align-items: center;
        display: flex;
        height: 100vh;
    }
    .wallpaper-register {
        background: url(https://images.pexels.com/photos/533671/pexels-photo-533671.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)
        no-repeat center center;
        background-size: cover;
        height: 100%;
        position: absolute;
        width: 100%;
        z-index: -1;
    }
    h1 {
        margin-bottom: 1.5rem;
        color:indigo;
    }

</style>
