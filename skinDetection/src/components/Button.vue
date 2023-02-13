<template>

    <!-- <button class="btn" @click="onPickFile">Upload Photo</button>
    <input
  type="file"
  style="display: none"
  ref="fileInput"
  accept="image/*"
  @change="onFilePicked"/> -->

  <div>
    <form>
      <input type="file" ref="fileInput" @change="upload"/>
    </form>
  </div>
   

</template>

<script>
import axios from 'axios';

export default {
    name: 'Button',
    data () {
    return {
      // image: null
    }
  },
  methods: {
//     onPickFile () {
//   this.$refs.fileInput.click()
// },
// onFilePicked (event) {
//   const files = event.target.files
//   let filename = files[0].name
//   const fileReader = new FileReader()
//   fileReader.addEventListener('load', () => {
//     this.imageUrl = fileReader.result
//   })
//   fileReader.readAsDataURL(files[0])
//   this.image = files[0]
// }, 
upload() {
      const input = this.$refs.fileInput
      const file = input.files[0]

      const formData = new FormData()
      formData.append('photo', file)

      axios.post('http://localhost:5000/api/photo/upload', formData).then(response => {
        console.log(response.data)
      })
    }


  }

 
}
</script>

<style scoped>


</style>
