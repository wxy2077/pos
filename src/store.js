import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  // 存储状态
      count: 1,
  },
  mutations: {
    // 只能用 mutations 和 actions 修改   区别  同步修改状态
      add(state,n){
          state.count+=n;
      },
      reduce(state){
          state.count--;
      },
  },
  actions: {
  // 异步 修改状态

  }
})
