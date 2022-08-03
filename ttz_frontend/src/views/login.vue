<template>
      
      <div id="content" style="height: 100vh;">
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
        
        <div class="" >
           <div class="" >
             
              <div class="grid place-items-center h-[70vh]">
                <div class="w-[400px] rounded overflow-hidden shadow-lg">
                  
                  <div class="px-6 py-4">
                    <div class="text-left"><router-link to='/'><i class="fa-solid fa-arrow-left-long hover:border-b-2 hover:border-black"></i></router-link></div>
                    <div class="font-bold text-xl mb-2 border-1" style="border-bottom: 1px solid black;">Sign in</div>
                    <!-- <p class="text-gray-700 text-base">
                      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatibus quia, nulla! Maiores et perferendis eaque, exercitationem praesentium nihil.
                    </p> -->
                    
                  <br>

                  <!-- <input v-model="username" type="text" class="input mb-3 mt-4 mr-2" style="width:200px;" placeholder="username" required>

                  <input v-model="password" type="password" class="md:flex appearance-none border-2 border-gray-400 rounded  py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-gray-100 focus:border-gray-900" style="width:200px;" placeholder="Password" required> -->
                  <div class="md:flex md:items-center my-6 ">
                      <div class="md:w-[120px] ml-[15px]">
                        <label class="block text-gray-500 font-bold md:text-right pr-4" for="inline-full-name">
                          Email:
                        </label>
                      </div>
                      <div class="md:w-[300px]">
                          <input v-model="username" class="md:flex appearance-none border-2 border-gray-400 rounded py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-0 focus:bg-gray-100 focus:border-orange-700 w-[200px]" type="email" placeholder="Email">
                      </div>
                  </div>
                  <div class="md:flex md:items-center mt-6 ">
                      <div class="md:w-[100px] ml-[19px]">
                        <label class="block text-gray-500 font-bold md:text-right pr-4" for="inline-full-name">
                          Password:
                        </label>
                      </div>
                      <div class="md:w-[300px]">
                          <input v-model="password" class="md:flex appearance-none border-2 border-gray-400 rounded py-2 px-4 text-gray-700 leading-tight focus:outline-none  focus:ring-0 focus:bg-gray-100 focus:border-orange-700 w-[200px]" type="password" placeholder="password">
                      </div>
                  </div>
                  <br>
                  <button class="bg-buttonAccent1 hover:bg-buttonAccentHover w-[270px] text-white font-bold py-2 mx-1 rounded" type="submit" @click="submit" >Sign in</button>
                  <br>
                  <p class="mt-3 text-sm">Don't have an account <span class="border-b-2 border-red-700 text-red-700 hover:text-red-500 hover:border-red-500 cursor-pointer"><router-link to='/register'>Sign up</router-link></span> here</p>
                  </div>
                  
                </div>
              </div>
              <!-- <div class="card bg-light" style="width:500px;height:300px;">
                  <h1 class="" style="font-size:20px; font-weight:700;"><p style="border-bottom:1px solid #DBDBDB;">Sign in</p></h1>
                  <br>

                  <input v-model="username" type="text" class="input mb-3 mt-4 mr-2" style="width:200px;" placeholder="username" required>

                  <input v-model="password" type="password" class="input mt-4 mb-3" style="width:200px;" placeholder="Password" required>
                  <br>

                  <button class="button btn-lg btn-primary mt-4 mb-4" type="submit" @click="submit" style="background-color: #26ADE4; color:white;">Sign in</button>
              </div> -->
            </div>
          </div>
        </div>
</template>

<script>
import api from "../../boot/axios"
import NavbarNotLoggedIn from "@/components/NavbarNotLoggedIn.vue"
import { notify } from "notiwind"


export default {
  name: "login",
  components: { NavbarNotLoggedIn },
  data(){
    return{
      username: '',
      password: '',
      currentUser: ''
    }
  },
  methods:{
    async submit(){
      var loginForm = {
          email: this.username,
          password: this.password
      };
      var jwtToken = ''
      await api.post('/auth/logins', loginForm, 
        {
          withCredentials: true
        }
      ).then(res => {
        jwtToken  = res.data

        if(res.status != 200){
            this.toastDanger()
            this.username = ''
            this.password = ''
            
          }

      })
      console.log(jwtToken);

       api.defaults.headers.common['Authorization'] = `Bearer ${jwtToken.token}`;
       localStorage.setItem('jwt', jwtToken.token)
       localStorage.setItem('r_token', jwtToken.r_token)
      //  localStorage.setItem('username', jwtToken.username);
       localStorage.setItem('email', jwtToken.email);
       localStorage.setItem('role', jwtToken.role);
       localStorage.setItem('position', jwtToken.position);
       localStorage.setItem('name', jwtToken.name);
       localStorage.setItem('id', jwtToken.id);


      //  alert(jwtToken.username)
         
          await api.get(`/auth/user/${jwtToken.id}/`
                ).then(res =>{
                    
                    
                    this.currentUser = res.data
                }).catch(err => console.log(err))
                  // console.log('yooo',this.userData)
                //Set Current User
                
          this.$store.commit('setCurrentUser', this.currentUser)
          this.$router.push({ name: 'Home'});
         

    },
    toastDanger(){
        notify({
        group: "danger",
        title: "Sign Up Failed",
        text: "User Credentials Does Not Match",
        }, 1500)
    },
  }
}
</script>

<style scoped>
  .card {
    margin: 60px auto; /* Added */
    float: none; /* Added */

    padding: 40px;
  }
</style>