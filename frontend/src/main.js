import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import VueResource from 'vue-resource'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'
import { Message, Notification } from "element-ui";

axios.defaults.baseURL = '/api'

Vue.prototype.$axios = axios
Vue.prototype.$message = Message
Vue.prototype.$notify = Notification
// axios.defaults.headers.post['Content-Type'] = 'application/json';

Vue.config.productionTip = false

Vue.use(ElementUI)
Vue.use(VueResource)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
