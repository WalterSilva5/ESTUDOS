import Vue from 'vue'
import Vue2Filters from 'vue2-filters'
import App from './App.vue'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
Vue.config.productionTip = false
Vue.use(Vue2Filters)
new Vue({
    render: h => h(App),
}).$mount('#app')