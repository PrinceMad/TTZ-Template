import { createStore } from 'vuex'

export default createStore({
  state: {
      currentUser: ''
  },
  getters: {
      getCurentUser: state => state.currentUser
  },
  mutations: {
      setCurrentUser(state,payload){
          state.currentUser = payload
      }
  },
  actions: {
  },
  modules: {
  }
})
