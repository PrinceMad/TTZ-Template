<template>
<div>
  <div>
    <Sidebar/>
  </div>

</div>

  
</template>
<script>
import Sidebar from '@/components/sidebar/Sidebar'
import {sidebarWidth} from '@/components/sidebar/state'


export default ({
  components: {Sidebar},
  setup(){
    return {sidebarWidth}
  },
  data(){
    return{    

    }
  },
  methods: {
  }
})
</script>