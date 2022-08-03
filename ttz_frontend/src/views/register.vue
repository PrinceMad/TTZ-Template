<template>
        <div class="" style="height:100vh;">
            <NavbarNotLoggedIn/>
            <NotificationGroup group="danger">
            <div class="fixed inset-0 flex items-start justify-end px-4 py-6 mt-[85vh] pointer-events-none">
                <div class="w-full max-w-sm">
                    <Notification
                        v-slot="{ notifications }"
                        enter="transform ease-out duration-300 transition"
                        enter-from="translate-y-2 opacity-0 sm:translate-y-0 sm:translate-x-4"
                        enter-to="translate-y-0 opacity-100 sm:translate-x-0"
                        leave="transition ease-in duration-500"
                        leave-from="opacity-100"
                        leave-to="opacity-0"
                        move="transition duration-500"
                        move-delay="delay-300"
                    >
                        <div
                        class="flex w-full max-w-sm mx-auto mt-4 overflow-hidden bg-white rounded-lg shadow-md"
                        v-for="notification in notifications"
                        :key="notification.id"
                        >
                        <div class="flex items-center justify-center w-12 bg-darkAccent">
                            <svg class="w-6 h-6 text-white fill-current" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
                            <path d="M20 3.33331C10.8 3.33331 3.33337 10.8 3.33337 20C3.33337 29.2 10.8 36.6666 20 36.6666C29.2 36.6666 36.6667 29.2 36.6667 20C36.6667 10.8 29.2 3.33331 20 3.33331ZM16.6667 28.3333L8.33337 20L10.6834 17.65L16.6667 23.6166L29.3167 10.9666L31.6667 13.3333L16.6667 28.3333Z" />
                            </svg>
                        </div>

                        <div class="px-4 py-2 -mx-3">
                            <div class="mx-3">
                            <span class="font-semibold text-black">{{ notification.title }}</span>
                            <p class="text-sm text-gray-600">{{ notification.text }}</p>
                            </div>
                        </div>
                        </div>
                        </Notification>
                    </div>
                </div>
            </NotificationGroup>
            <NotificationGroup group="success">
            <div class="fixed inset-0 flex items-start justify-end px-4 py-6 mt-[85vh] pointer-events-none">
                <div class="w-full max-w-sm">
                    <Notification
                        v-slot="{ notifications }"
                        enter="transform ease-out duration-300 transition"
                        enter-from="translate-y-2 opacity-0 sm:translate-y-0 sm:translate-x-4"
                        enter-to="translate-y-0 opacity-100 sm:translate-x-0"
                        leave="transition ease-in duration-500"
                        leave-from="opacity-100"
                        leave-to="opacity-0"
                        move="transition duration-500"
                        move-delay="delay-300"
                    >
                        <div
                        class="flex w-full max-w-sm mx-auto mt-4 overflow-hidden bg-white rounded-lg shadow-md"
                        v-for="notification in notifications"
                        :key="notification.id"
                        >
                        <div class="flex items-center justify-center w-12 bg-AccentCustomer">
                            <svg class="w-6 h-6 text-white fill-current" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
                            <path d="M20 3.33331C10.8 3.33331 3.33337 10.8 3.33337 20C3.33337 29.2 10.8 36.6666 20 36.6666C29.2 36.6666 36.6667 29.2 36.6667 20C36.6667 10.8 29.2 3.33331 20 3.33331ZM16.6667 28.3333L8.33337 20L10.6834 17.65L16.6667 23.6166L29.3167 10.9666L31.6667 13.3333L16.6667 28.3333Z" />
                            </svg>
                        </div>

                        <div class="px-4 py-2 -mx-3">
                            <div class="mx-3">
                            <span class="font-semibold text-buttonAccent1">{{ notification.title }}</span>
                            <p class="text-sm text-gray-600">{{ notification.text }}</p>
                            </div>
                        </div>
                        </div>
                        </Notification>
                    </div>
                </div>
            </NotificationGroup>
            <div class="grid place-items-center h-[80vh]">
                <div class="w-[600px] rounded overflow-hidden shadow-lg">
                    <div class="px-6 py-4">
                        <div class="text-left"><router-link to='/login'><i class="fa-solid fa-arrow-left-long hover:border-b-2 hover:border-black"></i></router-link></div>
                        
                        <div class="font-bold text-xl mb-2 border-1" style="border-bottom: 1px solid black;">Sign Up</div>
                        
                       
                        
                        <div class="md:flex md:items-center my-6 ">
                            <div class="md:w-[180px] ml-[15px]">
                                <label class="block text-gray-500 font-bold md:text-right pr-4" for="inline-full-name">
                                    Email:
                                </label>
                            </div>
                            <div class="md:w-[300px]">
                                <input v-model="email" class="md:flex appearance-none border-2 border-gray-400 rounded py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-0 focus:bg-gray-100 focus:border-orange-700 w-[200px]" type="email" placeholder="Email">
                            </div>
                        </div>
                        <div class="md:flex md:items-center my-6 ">
                            <div class="md:w-[180px] ml-[15px]">
                                <label class="block text-gray-500 font-bold md:text-right pr-4" for="inline-full-name">
                                    Password:
                                </label>
                            </div>
                            <div class="md:w-[300px]">
                                <input v-model="password" class="md:flex appearance-none border-2 border-gray-400 rounded py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-0 focus:bg-gray-100 focus:border-orange-700 w-[200px]" type="password" placeholder="Password">
                            </div>
                        </div>
                        <div class="md:flex md:items-center mt-6 ">
                            <div class="md:w-[180px] ml-[15px]">
                                <label class="block text-gray-500 font-bold md:text-right pr-4" for="inline-full-name">
                                    Confirm Password:
                                </label>
                            </div>
                            <div class="md:w-[300px]">
                                <input v-model="password_confirm" class="md:flex appearance-none border-2 border-gray-400 rounded py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-0 focus:bg-gray-100 focus:border-orange-700 w-[200px]" type="password" placeholder="Confirm Password">
                            </div>
                        </div>
                       
                       
                        <br>
                        
                        <button class="bg-buttonAccent1 hover:bg-buttonAccentHover w-[270px] text-white font-bold py-2 mx-1 rounded" type="submit" @click="submit()" >Sign Up</button>
                            
                        
                    </div>
                </div>
            </div>
              
        </div>
       
</template>

<script>
import api from "../../boot/axios"
import NavbarNotLoggedIn from "@/components/NavbarNotLoggedIn.vue"
import { notify } from "notiwind"



export default {
  name: "Register",
  components: { NavbarNotLoggedIn },
  data(){
    return{
      email: '',
      password: '',
      password_confirm: '',
      username: '',
      firstName: '',
      lastName: '',
      role: '',
      userList: '',
      emailTaken: false,
    }
  },
  async mounted(){
    
  },
  methods:{
    async submit(){
        
        this.emailTaken = false
        await api.get('/auth/user/').then(res =>{
            this.userList = res.data
        }).catch(err => console.log(err))
        console.log(this.userList)
        for(let i=0; i<this.userList.length; i++){
            if(this.userList[i].email==this.email){
                this.toastEmailFailed()
                this.emailTaken = true
            }else{
                this.emailTaken =false
            }
        }

        if(this.emailTaken == false){
            if(this.password == this.password_confirm){
                var regForm = {
                    email: this.email,
                    password: this.password,
                    password_confirm: this.password_confirm,
                    role: 1,
            };
        await api.post('/auth/registers', regForm).then((res) => {
          if(res.status == 200){
              this.showDetail = true
                console.log('user success')
                this.Toast() 
                    
                }else{
                    console.log('user failed')
                }
                    
                }).catch((err)=>{console.log(err)})
               

                this.email = ''
                this.password = ''
                this.password_confirm = ''
                this.$router.push('/login');
                    

            }else{
                this.toastDanger()
                this.password = ''
                this.password_confirm = ''
            }
        } 
    },
    Toast(){
        notify({
        group: "success",
        title: "Added",
        text: "User Account is Created",
        }, 1500)
    },
    toastDanger(){
        notify({
        group: "danger",
        title: "Failed",
        text: "Password Does Not Match",
        }, 1500)
    },
    toastEmailFailed(){
        notify({
        group: "danger",
        title: "Failed",
        text: "Email is already taken",
        }, 1500)
    }
   
  }
  
}
</script>

<style scoped>
  .card {
    margin: 0px auto; 
    float: none;

    padding: 40px;
  }
</style>
