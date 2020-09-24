import Vue from 'vue'
import App from './App.vue'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import VueSimpleAlert from "vue-simple-alert";
import Vue2Editor from 'vue2-editor'

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(Vue2Editor)
Vue.use(VueSimpleAlert)

let VueTruncate = require('vue-truncate-filter')
Vue.use(VueTruncate)

new Vue({
  router,
    data : {
    },
  render: h => h(App)
}).$mount('#app')
