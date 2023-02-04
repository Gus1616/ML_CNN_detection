<template>

    <button class="btn" @click="onPickFile">Upload Photo</button>
    <input
  type="file"
  style="display: none"
  ref="fileInput"
  accept="image/*"
  @change="onFilePicked"/>
   

</template>

<script>

export default {
    name: 'Button',
    data () {
    return {
      image: null
    }
  },
  methods: {
    onPickFile () {
  this.$refs.fileInput.click()
},
onFilePicked (event) {
  const files = event.target.files
  let filename = files[0].name
  const fileReader = new FileReader()
  fileReader.addEventListener('load', () => {
    this.imageUrl = fileReader.result
  })
  fileReader.readAsDataURL(files[0])
  this.image = files[0]
}

  }

 
}
</script>

<style scoped>


</style>
