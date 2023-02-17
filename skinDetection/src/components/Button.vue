<template>
  <div>
    <form>
      <input type="file" ref="fileInput" @change="upload"/>
    </form>
  </div>

  <div>
    <p>{{ message }}</p>
  </div>
   

</template>

<script>
import axios from 'axios';

export default {
    name: 'Button',
    data () {
    return {
      // image: null
      message: ''
    }
  },
  methods: {
upload() {
      const input = this.$refs.fileInput
      const file = input.files[0]

      const formData = new FormData()
      formData.append('photo', file)

      axios.post('http://localhost:5000/api/photo/upload', formData).then(response => {
        console.log(response.data)
        this.message = response.data.message
      })
    }


  }

 
}
</script>

<style scoped>


</style>
