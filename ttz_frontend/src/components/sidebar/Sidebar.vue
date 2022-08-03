<script>
import api from '../../../boot/axios'
import SidebarLink from './SidebarLink'
import { collapsed, toggleSidebar, sidebarWidth } from './state'
import axios from '../../../boot/axios'

export default {
  props: {},
  components: { SidebarLink },
  setup() {
    return { collapsed, toggleSidebar, sidebarWidth }
  },
  data() {
            return {
                showMenu: false,
                userNameSidebar: '',
                userData: '',
                userSet: '',
                userRole: '',
                delayTime: true,
                currentName: '',
                currentPos: ''
            }
        },
  created(){
      // this.userNameSidebar = localStorage.getItem("username")
      this.getUserType()
  },
  methods:{
    toggleShow() {
      this.showMenu = !this.showMenu;
    },
    async logout(){
            this.userNameSidebar = null;
            let r_token = localStorage.getItem('r_token');
            localStorage.removeItem('jwt');
            localStorage.removeItem('r_token');
            localStorage.removeItem('email');
            localStorage.removeItem('role');
            
            await api.post('/auth/logout', {'r_token': r_token}, {withCredentials: true});
            api.defaults.headers.common['Authorization'] = '';
            this.indx ++;
            this.userSet = ''
            localStorage.clear();
            this.$router.push('/');
           
        },
        async getUserType(){
                this.currentName = localStorage.getItem('name')
                this.currentPos = localStorage.getItem('position')
                this.userData = this.$store.getters.getCurentUser
                console.log(this.userData, 'mounted')
        },
        delaySidebar(){
          if(this.collapsed == false){
            setTimeout(()=>{
            this.delayTime = true
          },200)
          }else{
            this.delayTime = false
          } 
        },
  }
}
</script>

<template>
  <div class="sidebar" :style="{ width: sidebarWidth }">
    <h1>
      <span v-if="delayTime">
        <img src="@/assets/ttz.png" alt="TTZ" style="width:60%; margin-left:50px">
      </span>
      <span v-else style="font-weight:700"></span>
    </h1>


    

    <SidebarLink to="/home" icon="fas fa-home" style="font-size:20px; margin-top:70px;" @click.prevent="showMenu = false">Home</SidebarLink>
    

    <div style="" v-if="delayTime">
      <div style="position: fixed; bottom:50px; border-top: 1px solid #A4ADBA; width:225px;">
      <div style="float:left; margin-left:10px;">
        <p style="font-size:22px; color:#A4ADBA;font-weight:700"> {{currentName}}</p>
      </div>
      
      <div class="tooltip" style="float:right; margin-right:5px; margin-top:5px;">
        <!-- <span class="tooltiptext">Log Out</span> -->
        <!-- <a class="" @click="logout" style="font-size:22px; color:white;"><i class="fas fa-solid fa-arrow-right-from-bracket"></i></a> -->
        <a @click="logout" style=""><img class="logB" src="../../assets/logout_w.png" style=" text-align:center; cursor: pointer; width:17px;"></a>
      </div>
      
    </div>
    <div style="position: fixed; bottom:33px; width:190px;">
      <div style="float:left; margin-left:12px">
        <p style="font-size:18px; color:#A4ADBA;font-weight:500">@{{currentPos}}</p>
      </div>
    </div>
    </div>

    <span
      class="collapse-icon"
      :class="{ 'rotate-180': collapsed }"
      @click="toggleSidebar(); delaySidebar()"
    >
      <i class="fas fa-angle-double-left" />
    </span>
  </div>
</template>

<style>
:root {
  --sidebar-bg-color: #2E4150;
  --sidebar-item-hover: #83D0C8;
  --sidebar-item-active: #83D0C8;
}
</style>

<style scoped>
.sidebar {
  color: white;
  background-color: var(--sidebar-bg-color);

  float: left;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  bottom: 0;
  padding: 0.5em 0em 0.5em 0em;

  transition: 0.3s ease;

  display: flex;
  flex-direction: column;
}


.sidebar h1 {
  height: 2.5em;
}

.collapse-icon {
  position: absolute;
  bottom: 0;
  padding: 0.75em;

  color: rgba(255, 255, 255, 0.7);

  transition: 0.2s linear;
}

.rotate-180 {
  transform: rotate(180deg);
  transition: 0.2s linear;
}

.tooltip:hover .tooltiptext {
  visibility: visible;
}
.logB{
  width:20px;
}
.logB:hover{
  outline:solid;
  outline-color: white;
  outline-offset:2px;  
}
</style>
